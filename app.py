import ifcopenshell
import ifcopenshell.geom
import vtk

# Setup IfcOpenShell's geometry settings (using default settings)
settings = ifcopenshell.geom.settings()
settings.set(settings.USE_WORLD_COORDS, True)  # Use world coordinates for placement

# Load the IFC file
file_path = 'haus.ifc'
ifc_file = ifcopenshell.open(file_path)

# Create a VTK renderer, render window, and interactor
renderer = vtk.vtkRenderer()
render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)
render_window_interactor = vtk.vtkRenderWindowInteractor()
render_window_interactor.SetRenderWindow(render_window)


# Function to convert IfcOpenShell geometry to VTK format
def ifc_shape_to_vtk_actor(shape):
    verts = shape.geometry.verts
    faces = shape.geometry.faces

    # Convert vertices to VTK points
    points = vtk.vtkPoints()
    for i in range(0, len(verts), 3):
        points.InsertNextPoint(verts[i], verts[i + 1], verts[i + 2])

    # Create VTK poly data and add points and faces
    poly_data = vtk.vtkPolyData()
    poly_data.SetPoints(points)

    # Add faces to the geometry
    cells = vtk.vtkCellArray()
    for i in range(0, len(faces), 3):
        triangle = vtk.vtkTriangle()
        triangle.GetPointIds().SetId(0, faces[i])
        triangle.GetPointIds().SetId(1, faces[i + 1])
        triangle.GetPointIds().SetId(2, faces[i + 2])
        cells.InsertNextCell(triangle)

    poly_data.SetPolys(cells)

    # Create a mapper and actor for the shape
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(poly_data)

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    return actor


# Initialize a flag to see if any geometry is processed
geometry_added = False

# Loop through the IFC file and extract geometry for each geometric element
for element in ifc_file.by_type("IfcProduct"):
    try:
        if element.Representation is not None:
            # Create a shape representation for the element using IfcOpenShell
            print(f"Processing product {element.GlobalId} of type {element.is_a()}")
            shape = ifcopenshell.geom.create_shape(settings, element)

            # Convert the shape to a VTK actor and add to the renderer
            actor = ifc_shape_to_vtk_actor(shape)
            renderer.AddActor(actor)
            geometry_added = True  # Mark that we have successfully added geometry
        else:
            print(
                f"Skipping product {element.GlobalId} (Type: {element.is_a()}) due to missing geometry representation.")
    except Exception as e:
        print(f"Could not extract geometry for element {element.GlobalId}: {e}")

# Check if any geometry was added for rendering
if geometry_added:
    # Set up the camera and rendering window
    renderer.SetBackground(0.1, 0.2, 0.4)  # Set background color
    render_window.Render()

    # Start the interaction loop
    render_window_interactor.Start()
else:
    print("No geometry was added to the scene.")
