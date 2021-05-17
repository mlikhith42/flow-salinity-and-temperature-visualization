# state file generated using paraview version 5.7.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# trace generated using paraview version 5.7.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1061, 795]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [40.304264068603516, 20.007100105285645, -0.3974999836354982]
renderView1.HiddenLineRemoval = 1
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [40.304264068603516, 20.007100105285645, 55.028751317027634]
renderView1.CameraFocalPoint = [40.304264068603516, 20.007100105285645, -0.3974999836354982]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 14.34536943524998
renderView1.CameraParallelProjection = 1
renderView1.Background = [0.32, 0.34, 0.43]
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = None

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
netCDFReader1 = NetCDFReader(FileName=['/home/intel_lab3/Documents/GAVNitish/0001/COMBINED_2011013100.nc'])
netCDFReader1.Dimensions = '(Z_MIT40, YC, XG)'
netCDFReader1.SphericalCoordinates = 0

# create a new 'NetCDF Reader'
netCDFReader3 = NetCDFReader(FileName=['/home/intel_lab3/Documents/GAVNitish/0001/COMBINED_2011013100.nc'])
netCDFReader3.Dimensions = '(Z_MIT40, YG, XC)'
netCDFReader3.SphericalCoordinates = 0

# create a new 'XDMF Reader'
xDMFReader1 = XDMFReader(FileNames=['/home/intel_lab3/Documents/GAVNitish/0001/bathymetry.xmf'])
xDMFReader1.PointArrayStatus = ['depth']
xDMFReader1.GridStatus = ['Grid']

# create a new 'Warp By Scalar'
warpByScalar1 = WarpByScalar(Input=xDMFReader1)
warpByScalar1.Scalars = ['POINTS', '']
warpByScalar1.ScaleFactor = 0.00025

# create a new 'Threshold'
threshold1 = Threshold(Input=warpByScalar1)
threshold1.Scalars = ['POINTS', '']
threshold1.ThresholdRange = [-3073.121826171875, -0.0]

# create a new 'Resample To Image'
resampleToImage1 = ResampleToImage(Input=netCDFReader1)
resampleToImage1.UseInputBounds = 0
resampleToImage1.SamplingDimensions = [500, 500, 50]
resampleToImage1.SamplingBounds = [30.007099151611328, 49.967098236083984, 10.027099609375, 29.98710060119629, -3178.0, -2.0]

# create a new 'Resample To Image'
resampleToImage3 = ResampleToImage(Input=netCDFReader3)
resampleToImage3.UseInputBounds = 0
resampleToImage3.SamplingDimensions = [500, 500, 50]
resampleToImage3.SamplingBounds = [30.027099609375, 49.987098693847656, 10.007100105285645, 29.967100143432617, -3178.0, -2.0]

# create a new 'NetCDF Reader'
netCDFReader2 = NetCDFReader(FileName=['/home/intel_lab3/Documents/GAVNitish/0001/COMBINED_2011013100.nc'])
netCDFReader2.Dimensions = '(Z_MIT40, YC, XC)'
netCDFReader2.SphericalCoordinates = 0

# create a new 'Resample To Image'
resampleToImage2 = ResampleToImage(Input=netCDFReader2)
resampleToImage2.UseInputBounds = 0
resampleToImage2.SamplingDimensions = [500, 500, 50]
resampleToImage2.SamplingBounds = [30.027099609375, 49.987098693847656, 10.027099609375, 29.98710060119629, -3178.0, -2.0]

# create a new 'Append Attributes'
appendAttributes1 = AppendAttributes(Input=[resampleToImage1, resampleToImage3, resampleToImage2])

# create a new 'Calculator'
calculator1 = Calculator(Input=appendAttributes1)
calculator1.ResultArrayName = 'UVW'
calculator1.Function = 'U*iHat+V*jHat+W*kHat'

# create a new 'Calculator'
calculator2 = Calculator(Input=calculator1)
calculator2.ResultArrayName = 'Speed'
calculator2.Function = 'norm(UVW)'

# create a new 'Transform'
transform1 = Transform(Input=calculator2)
transform1.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform1.Transform.Scale = [1.0, 1.0, 0.00025]

# create a new 'Glyph'
glyph1 = Glyph(Input=transform1,
    GlyphType='Line')
glyph1.OrientationArray = ['POINTS', 'UVW']
glyph1.ScaleArray = ['POINTS', 'UVW']
glyph1.ScaleFactor = 1.996000099182129
glyph1.GlyphTransform = 'Transform2'
glyph1.GlyphMode = 'Uniform Spatial Distribution (Surface Sampling)'
glyph1.MaximumNumberOfSamplePoints = 110000
glyph1.Seed = 23948

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from xDMFReader1
xDMFReader1Display = Show(xDMFReader1, renderView1)

# get color transfer function/color map for 'depth'
depthLUT = GetColorTransferFunction('depth')
depthLUT.RGBPoints = [-3073.121826171875, 0.23137254902, 0.298039215686, 0.752941176471, -1536.0609130859375, 0.865, 0.865, 0.865, 1.0, 0.705882352941, 0.0156862745098, 0.149019607843]
depthLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'depth'
depthPWF = GetOpacityTransferFunction('depth')
depthPWF.Points = [-3073.121826171875, 0.0, 0.5, 0.0, -434.19189453125, 0.36764705181121826, 0.5, 0.0, -8.259357452392578, 0.29411765933036804, 0.5, 0.0, 1.0, 0.7426470518112183, 0.5, 0.0]
depthPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
xDMFReader1Display.Representation = 'Slice'
xDMFReader1Display.ColorArrayName = ['POINTS', 'depth']
xDMFReader1Display.LookupTable = depthLUT
xDMFReader1Display.OSPRayScaleArray = 'depth'
xDMFReader1Display.OSPRayScaleFunction = 'PiecewiseFunction'
xDMFReader1Display.SelectOrientationVectors = 'None'
xDMFReader1Display.ScaleFactor = 1.9960000000000002
xDMFReader1Display.SelectScaleArray = 'depth'
xDMFReader1Display.GlyphType = 'Arrow'
xDMFReader1Display.GlyphTableIndexArray = 'depth'
xDMFReader1Display.GaussianRadius = 0.0998
xDMFReader1Display.SetScaleArray = ['POINTS', 'depth']
xDMFReader1Display.ScaleTransferFunction = 'PiecewiseFunction'
xDMFReader1Display.OpacityArray = ['POINTS', 'depth']
xDMFReader1Display.OpacityTransferFunction = 'PiecewiseFunction'
xDMFReader1Display.DataAxesGrid = 'GridAxesRepresentation'
xDMFReader1Display.PolarAxes = 'PolarAxesRepresentation'
xDMFReader1Display.ScalarOpacityUnitDistance = 0.4486852963400412
xDMFReader1Display.ScalarOpacityFunction = depthPWF
xDMFReader1Display.IsosurfaceValues = [-1536.5609130859375]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
xDMFReader1Display.ScaleTransferFunction.Points = [-3073.121826171875, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
xDMFReader1Display.OpacityTransferFunction.Points = [-3073.121826171875, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

# show data from warpByScalar1
warpByScalar1Display = Show(warpByScalar1, renderView1)

# trace defaults for the display properties.
warpByScalar1Display.Representation = 'Surface'
warpByScalar1Display.ColorArrayName = ['POINTS', 'depth']
warpByScalar1Display.LookupTable = depthLUT
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

# show data from threshold1
threshold1Display = Show(threshold1, renderView1)

# trace defaults for the display properties.
threshold1Display.Representation = 'Surface'
threshold1Display.ColorArrayName = ['POINTS', 'depth']
threshold1Display.LookupTable = depthLUT
threshold1Display.OSPRayScaleArray = 'depth'
threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold1Display.SelectOrientationVectors = 'None'
threshold1Display.ScaleFactor = 1.996000099182129
threshold1Display.SelectScaleArray = 'depth'
threshold1Display.GlyphType = 'Arrow'
threshold1Display.GlyphTableIndexArray = 'depth'
threshold1Display.GaussianRadius = 0.09980000495910644
threshold1Display.SetScaleArray = ['POINTS', 'depth']
threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold1Display.OpacityArray = ['POINTS', 'depth']
threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
threshold1Display.PolarAxes = 'PolarAxesRepresentation'
threshold1Display.ScalarOpacityFunction = depthPWF
threshold1Display.ScalarOpacityUnitDistance = 0.44898147152501444

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold1Display.ScaleTransferFunction.Points = [-2518.233154296875, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold1Display.OpacityTransferFunction.Points = [-2518.233154296875, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

# show data from calculator2
calculator2Display = Show(calculator2, renderView1)

# trace defaults for the display properties.
calculator2Display.Representation = 'Outline'
calculator2Display.ColorArrayName = ['POINTS', '']
calculator2Display.OSPRayScaleArray = 'SALT'
calculator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator2Display.SelectOrientationVectors = 'Speed'
calculator2Display.ScaleFactor = 317.6
calculator2Display.SelectScaleArray = 'None'
calculator2Display.GlyphType = 'Arrow'
calculator2Display.GlyphTableIndexArray = 'None'
calculator2Display.GaussianRadius = 15.88
calculator2Display.SetScaleArray = ['POINTS', 'SALT']
calculator2Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator2Display.OpacityArray = ['POINTS', 'SALT']
calculator2Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator2Display.DataAxesGrid = 'GridAxesRepresentation'
calculator2Display.PolarAxes = 'PolarAxesRepresentation'
calculator2Display.ScalarOpacityUnitDistance = 13.796383430596622
calculator2Display.Slice = 24

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 42.44937234461689, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 42.44937234461689, 1.0, 0.5, 0.0]

# show data from transform1
transform1Display = Show(transform1, renderView1)

# trace defaults for the display properties.
transform1Display.Representation = 'Outline'
transform1Display.ColorArrayName = ['POINTS', '']
transform1Display.OSPRayScaleArray = 'SALT'
transform1Display.OSPRayScaleFunction = 'PiecewiseFunction'
transform1Display.SelectOrientationVectors = 'Speed'
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
glyph1Display = Show(glyph1, renderView1)

# get color transfer function/color map for 'UVW'
uVWLUT = GetColorTransferFunction('UVW')
uVWLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.5431757861441078, 0.865003, 0.865003, 0.865003, 1.0863515722882156, 0.705882, 0.0156863, 0.14902]
uVWLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = ['POINTS', 'UVW']
glyph1Display.LookupTable = uVWLUT
glyph1Display.OSPRayScaleArray = 'SALT'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'None'
glyph1Display.ScaleFactor = 2.017947769165039
glyph1Display.SelectScaleArray = 'None'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'None'
glyph1Display.GaussianRadius = 0.10089738845825195
glyph1Display.SetScaleArray = ['POINTS', 'SALT']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'SALT']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 40.65401896585767, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 40.65401896585767, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color transfer function/color map for 'TEMP'
tEMPLUT = GetColorTransferFunction('TEMP')
tEMPLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 15.247573660473684, 0.865003, 0.865003, 0.865003, 30.495147320947368, 0.705882, 0.0156863, 0.14902]
tEMPLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for tEMPLUT in view renderView1
tEMPLUTColorBar = GetScalarBar(tEMPLUT, renderView1)
tEMPLUTColorBar.WindowLocation = 'UpperRightCorner'
tEMPLUTColorBar.Title = 'TEMP'
tEMPLUTColorBar.ComponentTitle = ''

# set color bar visibility
tEMPLUTColorBar.Visibility = 0

# get color legend/bar for depthLUT in view renderView1
depthLUTColorBar = GetScalarBar(depthLUT, renderView1)
depthLUTColorBar.WindowLocation = 'UpperRightCorner'
depthLUTColorBar.Title = 'depth'
depthLUTColorBar.ComponentTitle = ''

# set color bar visibility
depthLUTColorBar.Visibility = 0

# get color legend/bar for uVWLUT in view renderView1
uVWLUTColorBar = GetScalarBar(uVWLUT, renderView1)
uVWLUTColorBar.WindowLocation = 'UpperLeftCorner'
uVWLUTColorBar.Title = 'UVW'
uVWLUTColorBar.ComponentTitle = 'Magnitude'

# set color bar visibility
uVWLUTColorBar.Visibility = 1

# get color transfer function/color map for 'Gradients'
gradientsLUT = GetColorTransferFunction('Gradients')
gradientsLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 957.4928895818076, 0.865003, 0.865003, 0.865003, 1914.9857791636152, 0.705882, 0.0156863, 0.14902]
gradientsLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for gradientsLUT in view renderView1
gradientsLUTColorBar = GetScalarBar(gradientsLUT, renderView1)
gradientsLUTColorBar.Title = 'Gradients'
gradientsLUTColorBar.ComponentTitle = 'Magnitude'

# set color bar visibility
gradientsLUTColorBar.Visibility = 0

# hide data in view
Hide(xDMFReader1, renderView1)

# hide data in view
Hide(warpByScalar1, renderView1)

# hide data in view
Hide(threshold1, renderView1)

# hide data in view
Hide(calculator2, renderView1)

# hide data in view
Hide(transform1, renderView1)

# show color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'TEMP'
tEMPPWF = GetOpacityTransferFunction('TEMP')
tEMPPWF.Points = [0.0, 0.0, 0.5, 0.0, 30.495147320947368, 1.0, 0.5, 0.0]
tEMPPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'UVW'
uVWPWF = GetOpacityTransferFunction('UVW')
uVWPWF.Points = [0.0, 0.0, 0.5, 0.0, 1.0863515722882156, 1.0, 0.5, 0.0]
uVWPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'Gradients'
gradientsPWF = GetOpacityTransferFunction('Gradients')
gradientsPWF.Points = [0.0, 0.0, 0.5, 0.0, 1914.9857791636152, 1.0, 0.5, 0.0]
gradientsPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(glyph1)
# ----------------------------------------------------------------