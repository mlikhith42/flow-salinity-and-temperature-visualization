# state file generated using paraview version 5.8.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# trace generated using paraview version 5.8.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1058, 492]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [39.987098693847656, 20.007100105285645, -0.39749999999999996]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [39.7892984316107, 19.45498051522635, 24.33704226181558]
renderView1.CameraFocalPoint = [41.09431104731354, 18.52302095548856, 3.3656051703276932]
renderView1.CameraViewUp = [0.5564253348404522, 0.830894433931965, -0.002299219121797688]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 14.119433762067587
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1
path= '/home/Dittu/Documents/Masters/Sem1/GAV/0001/COMBINED_2011013100.nc'
SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
netCDFReader1 = NetCDFReader(FileName=[path])
netCDFReader1.Dimensions = '(Z_MIT40, YC, XG)'
netCDFReader1.SphericalCoordinates = 0

# create a new 'Resample To Image'
resampleToImage3 = ResampleToImage(Input=netCDFReader1)
resampleToImage3.UseInputBounds = 0
resampleToImage3.SamplingDimensions = [500, 500, 50]
resampleToImage3.SamplingBounds = [30.007099151611328, 49.967098236083984, 10.027099609375, 29.98710060119629, -3178.0, -2.0]

# create a new 'NetCDF Reader'
netCDFReader2 = NetCDFReader(FileName=[path])
netCDFReader2.Dimensions = '(Z_MIT40, YC, XC)'
netCDFReader2.SphericalCoordinates = 0

# create a new 'Resample To Image'
resampleToImage2 = ResampleToImage(Input=netCDFReader2)
resampleToImage2.UseInputBounds = 0
resampleToImage2.SamplingDimensions = [500, 500, 50]
resampleToImage2.SamplingBounds = [30.027099609375, 49.987098693847656, 10.027099609375, 29.98710060119629, -3178.0, -2.0]

# create a new 'NetCDF Reader'
netCDFReader3 = NetCDFReader(FileName=[path])
netCDFReader3.Dimensions = '(Z_MIT40, YG, XC)'
netCDFReader3.SphericalCoordinates = 0

# create a new 'Resample To Image'
resampleToImage1 = ResampleToImage(Input=netCDFReader3)
resampleToImage1.UseInputBounds = 0
resampleToImage1.SamplingDimensions = [500, 500, 50]
resampleToImage1.SamplingBounds = [30.027099609375, 49.987098693847656, 10.007100105285645, 29.967100143432617, -3178.0, -2.0]

# create a new 'Append Attributes'
appendAttributes1 = AppendAttributes(Input=[resampleToImage3, resampleToImage1, resampleToImage2])

# create a new 'Calculator'
calculator1 = Calculator(Input=appendAttributes1)
calculator1.ResultArrayName = 'UVW'
calculator1.Function = 'U*iHat+V*jHat+W*kHat'

# create a new 'Transform'
transform1 = Transform(Input=calculator1)
transform1.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform1.Transform.Scale = [1.0, 1.0, 0.00025]

# create a new 'XDMF Reader'
xDMFReader1 = XDMFReader(FileNames=['/home/Dittu/Documents/Masters/Sem1/GAV/0001/bathymetry.xmf'])
xDMFReader1.PointArrayStatus = ['depth']
xDMFReader1.GridStatus = ['Grid']

# create a new 'Warp By Scalar'
warpByScalar1 = WarpByScalar(Input=xDMFReader1)
warpByScalar1.Scalars = ['POINTS', 'depth']
warpByScalar1.ScaleFactor = 0.00025

# create a new 'Threshold'
threshold1 = Threshold(Input=warpByScalar1)
threshold1.Scalars = ['POINTS', 'depth']
threshold1.ThresholdRange = [-3073.121826171875, -0.01]

# create a new 'Glyph'
glyph1 = Glyph(Input=transform1,
    GlyphType='Arrow')
glyph1.OrientationArray = ['POINTS', 'UVW']
glyph1.ScaleArray = ['POINTS', 'UVW']
glyph1.ScaleFactor = 1.996000099182129
glyph1.GlyphTransform = 'Transform2'
glyph1.GlyphMode = 'Uniform Spatial Distribution (Surface Sampling)'
glyph1.MaximumNumberOfSamplePoints = 70000
glyph1.Seed = 23948

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from warpByScalar1
warpByScalar1Display = Show(warpByScalar1, renderView1, 'StructuredGridRepresentation')

# get color transfer function/color map for 'depth'
depthLUT = GetColorTransferFunction('depth')
depthLUT.RGBPoints = [-3073.121826171875, 0.0, 0.0, 0.0, 0.0, 0.43, 0.851, 0.486]
depthLUT.ColorSpace = 'RGB'
depthLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'depth'
depthPWF = GetOpacityTransferFunction('depth')
depthPWF.Points = [-3073.121826171875, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]
depthPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
warpByScalar1Display.Representation = 'Surface'
warpByScalar1Display.ColorArrayName = ['POINTS', 'depth']
warpByScalar1Display.LookupTable = depthLUT
warpByScalar1Display.Opacity = 0.47
warpByScalar1Display.OSPRayScaleArray = 'depth'
warpByScalar1Display.OSPRayScaleFunction = 'PiecewiseFunction'
warpByScalar1Display.SelectOrientationVectors = 'None'
warpByScalar1Display.ScaleFactor = 1.996000099182129
warpByScalar1Display.SelectScaleArray = 'depth'
warpByScalar1Display.GlyphType = 'Arrow'
warpByScalar1Display.GlyphTableIndexArray = 'depth'
warpByScalar1Display.GaussianRadius = 0.09980000495910644
warpByScalar1Display.SetScaleArray = ['POINTS', 'depth']
warpByScalar1Display.ScaleTransferFunction = 'PiecewiseFunction'
warpByScalar1Display.OpacityArray = ['POINTS', 'depth']
warpByScalar1Display.OpacityTransferFunction = 'PiecewiseFunction'
warpByScalar1Display.DataAxesGrid = 'GridAxesRepresentation'
warpByScalar1Display.PolarAxes = 'PolarAxesRepresentation'
warpByScalar1Display.ScalarOpacityFunction = depthPWF
warpByScalar1Display.ScalarOpacityUnitDistance = 0.4488514546883703

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
warpByScalar1Display.ScaleTransferFunction.Points = [-3073.121826171875, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
warpByScalar1Display.OpacityTransferFunction.Points = [-3073.121826171875, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

# show data from transform1
transform1Display = Show(transform1, renderView1, 'StructuredGridRepresentation')

# trace defaults for the display properties.
transform1Display.Representation = 'Outline'
transform1Display.ColorArrayName = ['POINTS', '']
transform1Display.OSPRayScaleArray = 'SALT'
transform1Display.OSPRayScaleFunction = 'PiecewiseFunction'
transform1Display.SelectOrientationVectors = 'UVW'
transform1Display.ScaleFactor = 1.996000099182129
transform1Display.SelectScaleArray = 'None'
transform1Display.GlyphType = 'Arrow'
transform1Display.GlyphTableIndexArray = 'None'
transform1Display.GaussianRadius = 0.09980000495910644
transform1Display.SetScaleArray = ['POINTS', 'SALT']
transform1Display.ScaleTransferFunction = 'PiecewiseFunction'
transform1Display.OpacityArray = ['POINTS', 'SALT']
transform1Display.OpacityTransferFunction = 'PiecewiseFunction'
transform1Display.DataAxesGrid = 'GridAxesRepresentation'
transform1Display.PolarAxes = 'PolarAxesRepresentation'
transform1Display.ScalarOpacityUnitDistance = 0.12266336815460342

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
transform1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 42.44937234461689, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
transform1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 42.44937234461689, 1.0, 0.5, 0.0]

# show data from glyph1
glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'TEMP'
tEMPLUT = GetColorTransferFunction('TEMP')
tEMPLUT.RGBPoints = [25.0, 0.231373, 0.298039, 0.752941, 27.82572638625671, 0.865003, 0.865003, 0.865003, 30.651452772513426, 0.705882, 0.0156863, 0.14902]
tEMPLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = ['POINTS', 'TEMP']
glyph1Display.LookupTable = tEMPLUT
glyph1Display.Opacity = 0.9
glyph1Display.OSPRayScaleArray = 'SALT'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'None'
glyph1Display.ScaleFactor = 2.060654067993164
glyph1Display.SelectScaleArray = 'None'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'None'
glyph1Display.GaussianRadius = 0.1030327033996582
glyph1Display.SetScaleArray = ['POINTS', 'SALT']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'SALT']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 42.42023602888756, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 42.42023602888756, 1.0, 0.5, 0.0]

# show data from threshold1
threshold1Display = Show(threshold1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold1Display.Representation = 'Surface'
threshold1Display.ColorArrayName = ['POINTS', 'depth']
threshold1Display.LookupTable = depthLUT
threshold1Display.OSPRayScaleArray = 'depth'
threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold1Display.SelectOrientationVectors = 'None'
threshold1Display.ScaleFactor = 1.907999897003174
threshold1Display.SelectScaleArray = 'depth'
threshold1Display.GlyphType = 'Arrow'
threshold1Display.GlyphTableIndexArray = 'depth'
threshold1Display.GaussianRadius = 0.0953999948501587
threshold1Display.SetScaleArray = ['POINTS', 'depth']
threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold1Display.OpacityArray = ['POINTS', 'depth']
threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
threshold1Display.PolarAxes = 'PolarAxesRepresentation'
threshold1Display.ScalarOpacityFunction = depthPWF
threshold1Display.ScalarOpacityUnitDistance = 0.7891851437624806

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold1Display.ScaleTransferFunction.Points = [-3073.121826171875, 0.0, 0.5, 0.0, -20.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold1Display.OpacityTransferFunction.Points = [-3073.121826171875, 0.0, 0.5, 0.0, -20.0, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for depthLUT in view renderView1
depthLUTColorBar = GetScalarBar(depthLUT, renderView1)
depthLUTColorBar.Title = 'depth'
depthLUTColorBar.ComponentTitle = ''

# set color bar visibility
depthLUTColorBar.Visibility = 1

# get color legend/bar for tEMPLUT in view renderView1
tEMPLUTColorBar = GetScalarBar(tEMPLUT, renderView1)
tEMPLUTColorBar.WindowLocation = 'UpperRightCorner'
tEMPLUTColorBar.Title = 'TEMP'
tEMPLUTColorBar.ComponentTitle = ''

# set color bar visibility
tEMPLUTColorBar.Visibility = 1

# get color transfer function/color map for 'SALT'
sALTLUT = GetColorTransferFunction('SALT')
sALTLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 21.21011801444378, 0.865003, 0.865003, 0.865003, 42.42023602888756, 0.705882, 0.0156863, 0.14902]
sALTLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for sALTLUT in view renderView1
sALTLUTColorBar = GetScalarBar(sALTLUT, renderView1)
sALTLUTColorBar.WindowLocation = 'UpperRightCorner'
sALTLUTColorBar.Title = 'SALT'
sALTLUTColorBar.ComponentTitle = ''

# set color bar visibility
sALTLUTColorBar.Visibility = 0

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')
uLUT.RGBPoints = [-0.699057016208272, 0.231373, 0.298039, 0.752941, -0.024269339544376156, 0.865003, 0.865003, 0.865003, 0.6505183371195197, 0.705882, 0.0156863, 0.14902]
uLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for uLUT in view renderView1
uLUTColorBar = GetScalarBar(uLUT, renderView1)
uLUTColorBar.WindowLocation = 'UpperRightCorner'
uLUTColorBar.Title = 'U'
uLUTColorBar.ComponentTitle = ''

# set color bar visibility
uLUTColorBar.Visibility = 0

# show color legend
warpByScalar1Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(warpByScalar1, renderView1)

# hide data in view
Hide(transform1, renderView1)

# show color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# show color legend
threshold1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'U'
uPWF = GetOpacityTransferFunction('U')
uPWF.Points = [-0.699057016208272, 0.0, 0.5, 0.0, 0.6505183371195197, 1.0, 0.5, 0.0]
uPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'SALT'
sALTPWF = GetOpacityTransferFunction('SALT')
sALTPWF.Points = [0.0, 0.0, 0.5, 0.0, 42.42023602888756, 1.0, 0.5, 0.0]
sALTPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'TEMP'
tEMPPWF = GetOpacityTransferFunction('TEMP')
tEMPPWF.Points = [25.0, 0.0, 0.5, 0.0, 30.651452772513426, 1.0, 0.5, 0.0]
tEMPPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(glyph1)
# ----------------------------------------------------------------
