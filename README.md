# IFC to VTK 3D Viewer in Python

This script allows you to visualize an IFC (Industry Foundation Classes) file by converting its geometry to VTK (Visualization Toolkit) format. It uses the `IfcOpenShell` library to parse IFC geometry and the `VTK` library to render the resulting 3D shapes in an interactive window.

Sample IFC Files: https://www.steptools.com/docs/stpfiles/ifc/

## Prerequisites

Before running this script, make sure to install the necessary libraries:

- **IfcOpenShell**: A Python library for parsing IFC files.
- **VTK (Visualization Toolkit)**: A library for 3D computer graphics, image processing, and visualization.

You can install these libraries using pip:

```bash
pip install ifcopenshell vtk
```

Ensure that you have an IFC file to use as input. In this example, the script references a file named `haus.ifc`.

## How It Works

1. **IFC Geometry Loading**:
    - The script loads the IFC file using `IfcOpenShell`.
    - IFC Products with geometric representations are processed.
  
2. **Geometry Conversion**:
    - For each geometric product, the geometry is extracted using `IfcOpenShell`.
    - The geometry's vertices and faces are converted into VTK-compatible format (via `vtkPoints` and `vtkCellArray`).
    - A VTK actor is created for each element and added to the renderer.

3. **VTK Visualization**:
    - The script sets up a VTK rendering environment with a renderer, render window, and interactor.
    - The converted geometry is rendered using VTK in an interactive window.
  
4. **Interaction**:
    - The render window starts an interaction loop, allowing users to pan, zoom, and rotate the 3D model.

## Usage

1. Make sure you have an IFC file in the same directory as the script or adjust the path accordingly in the `file_path` variable:
   ```python
   file_path = 'haus.ifc'  # Replace with the path to your IFC file
   ```

2. Run the script:
   ```bash
   python script.py
   ```

3. If there is geometry available in the IFC file, a VTK interactive window will display the 3D visualization. If not, the script will output a message indicating that no geometry was found.

## Key Sections of the Script

- **IFC File Loading**: Loads the IFC file and iterates over all products.
- **Geometry Conversion**: Uses `IfcOpenShell` to extract geometry and convert it to VTK-compatible format.
- **VTK Rendering**: Sets up the VTK renderer, render window, and interactor for 3D visualization.

## Example Output

- The script outputs the Global IDs and types of products being processed.
- The VTK window opens with an interactive 3D view of the loaded IFC geometry.

## Potential Errors

- If the IFC file does not contain geometric data for certain products, the script will skip those products and notify you via the console.
- Errors during geometry extraction are caught, and a message is printed with the product ID and error details.
