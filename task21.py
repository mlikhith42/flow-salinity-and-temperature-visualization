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
renderView1.CenterOfRotation = [249.5, 249.5, 24.5]
renderView1.HiddenLineRemoval = 1
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-375.9529432115278, -595.5205429329201, 897.5855159199909]
renderView1.CameraFocalPoint = [249.5, 249.5, 24.500000000000053]
renderView1.CameraViewUp = [-0.10160806668213357, 0.7502289289010444, 0.6533240811611882]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 353.6958439111209
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
netCDFReader3 = NetCDFReader(FileName=['/home/intel_lab3/Documents/GAVNitish/0001/COMBINED_2011013100.nc'])
netCDFReader3.Dimensions = '(Z_MIT40, YC, XC)'
netCDFReader3.SphericalCoordinates = 0

# create a new 'XDMF Reader'
xDMFReader1 = XDMFReader(FileNames=['/home/intel_lab3/Documents/GAVNitish/0001/bathymetry.xmf'])
xDMFReader1.PointArrayStatus = ['depth']
xDMFReader1.GridStatus = ['Grid']

# create a new 'NetCDF Reader'
netCDFReader1 = NetCDFReader(FileName=['/home/intel_lab3/Documents/GAVNitish/0001/COMBINED_2011013100.nc'])
netCDFReader1.Dimensions = '(Z_MIT40, YC, XG)'
netCDFReader1.SphericalCoordinates = 0

# create a new 'Resample To Image'
resampleToImage3 = ResampleToImage(Input=netCDFReader3)
resampleToImage3.UseInputBounds = 0
resampleToImage3.SamplingDimensions = [500, 500, 50]
resampleToImage3.SamplingBounds = [30.027099609375, 49.987098693847656, 10.027099609375, 29.98710060119629, -3178.0, -2.0]

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

# create a new 'NetCDF Reader'
netCDFReader2 = NetCDFReader(FileName=['/home/intel_lab3/Documents/GAVNitish/0001/COMBINED_2011013100.nc'])
netCDFReader2.Dimensions = '(Z_MIT40, YG, XC)'
netCDFReader2.SphericalCoordinates = 0

# create a new 'Resample To Image'
resampleToImage2 = ResampleToImage(Input=netCDFReader2)
resampleToImage2.UseInputBounds = 0
resampleToImage2.SamplingDimensions = [500, 500, 50]
resampleToImage2.SamplingBounds = [30.027099609375, 49.987098693847656, 10.007100105285645, 29.967100143432617, -3178.0, -2.0]

# create a new 'Append Attributes'
appendAttributes1 = AppendAttributes(Input=[resampleToImage1, resampleToImage2, resampleToImage3])

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

# create a new 'Gradient'
grad_temp = Gradient(Input=appendAttributes1)
grad_temp.SelectInputScalars = ['POINTS', 'TEMP']

# create a new 'Threshold'
threshold3 = Threshold(Input=grad_temp)
threshold3.Scalars = ['POINTS', 'TEMP']
threshold3.ThresholdRange = [0.0, 31.171789593317612]

# create a new 'Gradient'
grad_salt = Gradient(Input=appendAttributes1)
grad_salt.SelectInputScalars = ['POINTS', 'SALT']

# create a new 'Threshold'
threshold2 = Threshold(Input=grad_salt)
threshold2.Scalars = ['POINTS', 'SALT']
threshold2.ThresholdRange = [0.1, 42.44937234461689]

# create a new 'Append Attributes'
appendAttributes2 = AppendAttributes(Input=[grad_temp, grad_salt])

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

# show data from grad_salt
grad_saltDisplay = Show(grad_salt, renderView1)

# get color transfer function/color map for 'SALT'
sALTLUT = GetColorTransferFunction('SALT')
sALTLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 21.224686172308445, 0.865003, 0.865003, 0.865003, 42.44937234461689, 0.705882, 0.0156863, 0.14902]
sALTLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'SALT'
sALTPWF = GetOpacityTransferFunction('SALT')
sALTPWF.Points = [0.0, 0.0, 0.5, 0.0, 42.44937234461689, 1.0, 0.5, 0.0]
sALTPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
grad_saltDisplay.Representation = 'Surface'
grad_saltDisplay.ColorArrayName = ['POINTS', 'SALT']
grad_saltDisplay.LookupTable = sALTLUT
grad_saltDisplay.OSPRayScaleArray = 'ImageScalarsGradient'
grad_saltDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
grad_saltDisplay.SelectOrientationVectors = 'ImageScalarsGradient'
grad_saltDisplay.ScaleFactor = 49.900000000000006
grad_saltDisplay.SelectScaleArray = 'ImageScalarsGradient'
grad_saltDisplay.GlyphType = 'Arrow'
grad_saltDisplay.GlyphTableIndexArray = 'ImageScalarsGradient'
grad_saltDisplay.GaussianRadius = 2.495
grad_saltDisplay.SetScaleArray = ['POINTS', 'ImageScalarsGradient']
grad_saltDisplay.ScaleTransferFunction = 'PiecewiseFunction'
grad_saltDisplay.OpacityArray = ['POINTS', 'ImageScalarsGradient']
grad_saltDisplay.OpacityTransferFunction = 'PiecewiseFunction'
grad_saltDisplay.DataAxesGrid = 'GridAxesRepresentation'
grad_saltDisplay.PolarAxes = 'PolarAxesRepresentation'
grad_saltDisplay.ScalarOpacityUnitDistance = 3.0727523672358505
grad_saltDisplay.ScalarOpacityFunction = sALTPWF
grad_saltDisplay.IsosurfaceValues = [1.1696214080178038]
grad_saltDisplay.Slice = 24

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
grad_saltDisplay.ScaleTransferFunction.Points = [-528.2779358300792, 0.0, 0.5, 0.0, 530.6171786461149, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
grad_saltDisplay.OpacityTransferFunction.Points = [-528.2779358300792, 0.0, 0.5, 0.0, 530.6171786461149, 1.0, 0.5, 0.0]

# show data from grad_temp
grad_tempDisplay = Show(grad_temp, renderView1)

# get color transfer function/color map for 'TEMP'
tEMPLUT = GetColorTransferFunction('TEMP')
tEMPLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 15.585894796658806, 0.865003, 0.865003, 0.865003, 31.171789593317612, 0.705882, 0.0156863, 0.14902]
tEMPLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'TEMP'
tEMPPWF = GetOpacityTransferFunction('TEMP')
tEMPPWF.Points = [0.0, 0.0, 0.5, 0.0, 31.171789593317612, 1.0, 0.5, 0.0]
tEMPPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
grad_tempDisplay.Representation = 'Surface'
grad_tempDisplay.ColorArrayName = ['POINTS', 'TEMP']
grad_tempDisplay.LookupTable = tEMPLUT
grad_tempDisplay.OSPRayScaleArray = 'ImageScalarsGradient'
grad_tempDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
grad_tempDisplay.SelectOrientationVectors = 'ImageScalarsGradient'
grad_tempDisplay.ScaleFactor = 49.900000000000006
grad_tempDisplay.SelectScaleArray = 'ImageScalarsGradient'
grad_tempDisplay.GlyphType = 'Arrow'
grad_tempDisplay.GlyphTableIndexArray = 'ImageScalarsGradient'
grad_tempDisplay.GaussianRadius = 2.495
grad_tempDisplay.SetScaleArray = ['POINTS', 'ImageScalarsGradient']
grad_tempDisplay.ScaleTransferFunction = 'PiecewiseFunction'
grad_tempDisplay.OpacityArray = ['POINTS', 'ImageScalarsGradient']
grad_tempDisplay.OpacityTransferFunction = 'PiecewiseFunction'
grad_tempDisplay.DataAxesGrid = 'GridAxesRepresentation'
grad_tempDisplay.PolarAxes = 'PolarAxesRepresentation'
grad_tempDisplay.ScalarOpacityUnitDistance = 3.0727523672358505
grad_tempDisplay.ScalarOpacityFunction = tEMPPWF
grad_tempDisplay.IsosurfaceValues = [0.16745334622257246]
grad_tempDisplay.Slice = 24

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
grad_tempDisplay.ScaleTransferFunction.Points = [-389.31248109641166, 0.0, 0.5, 0.0, 389.64738778885675, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
grad_tempDisplay.OpacityTransferFunction.Points = [-389.31248109641166, 0.0, 0.5, 0.0, 389.64738778885675, 1.0, 0.5, 0.0]

# show data from appendAttributes2
appendAttributes2Display = Show(appendAttributes2, renderView1)

# trace defaults for the display properties.
appendAttributes2Display.Representation = 'Points'
appendAttributes2Display.ColorArrayName = ['POINTS', 'TEMP']
appendAttributes2Display.LookupTable = tEMPLUT
appendAttributes2Display.OSPRayScaleArray = 'ImageScalarsGradient'
appendAttributes2Display.OSPRayScaleFunction = 'PiecewiseFunction'
appendAttributes2Display.SelectOrientationVectors = 'ImageScalarsGradient'
appendAttributes2Display.ScaleFactor = 49.900000000000006
appendAttributes2Display.SelectScaleArray = 'ImageScalarsGradient'
appendAttributes2Display.GlyphType = 'Arrow'
appendAttributes2Display.GlyphTableIndexArray = 'ImageScalarsGradient'
appendAttributes2Display.GaussianRadius = 2.495
appendAttributes2Display.SetScaleArray = ['POINTS', 'ImageScalarsGradient']
appendAttributes2Display.ScaleTransferFunction = 'PiecewiseFunction'
appendAttributes2Display.OpacityArray = ['POINTS', 'ImageScalarsGradient']
appendAttributes2Display.OpacityTransferFunction = 'PiecewiseFunction'
appendAttributes2Display.DataAxesGrid = 'GridAxesRepresentation'
appendAttributes2Display.PolarAxes = 'PolarAxesRepresentation'
appendAttributes2Display.ScalarOpacityUnitDistance = 3.0727523672358505
appendAttributes2Display.ScalarOpacityFunction = tEMPPWF
appendAttributes2Display.IsosurfaceValues = [0.16745334622257246]
appendAttributes2Display.Slice = 24

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
appendAttributes2Display.ScaleTransferFunction.Points = [-389.31248109641166, 0.0, 0.5, 0.0, 389.64738778885675, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
appendAttributes2Display.OpacityTransferFunction.Points = [-389.31248109641166, 0.0, 0.5, 0.0, 389.64738778885675, 1.0, 0.5, 0.0]

# show data from threshold2
threshold2Display = Show(threshold2, renderView1)

# get color transfer function/color map for 'ImageScalarsGradient'
imageScalarsGradientLUT = GetColorTransferFunction('ImageScalarsGradient')
imageScalarsGradientLUT.RGBPoints = [0.05508209364378967, 1.0, 1.0, 1.0, 0.06838816885935187, 0.113725, 0.0235294, 0.45098, 0.0818510225746863, 0.105882, 0.0509804, 0.509804, 0.09272067731426116, 0.0392157, 0.0392157, 0.560784, 0.10464932220198743, 0.0313725, 0.0980392, 0.6, 0.11768020100375673, 0.0431373, 0.164706, 0.639216, 0.13930553412773553, 0.054902, 0.243137, 0.678431, 0.1742305663883354, 0.054902, 0.317647, 0.709804, 0.22939194804089194, 0.0509804, 0.396078, 0.741176, 0.2741726538497803, 0.0392157, 0.466667, 0.768627, 0.3276952166849003, 0.0313725, 0.537255, 0.788235, 0.3947305500737896, 0.0313725, 0.615686, 0.811765, 0.47766348157851074, 0.0235294, 0.709804, 0.831373, 0.5780208720567882, 0.0509804, 0.8, 0.85098, 0.6767532082502892, 0.0705882, 0.854902, 0.870588, 0.7836806812170755, 0.262745, 0.901961, 0.862745, 0.8910135088159515, 0.423529, 0.941176, 0.87451, 1.0861532167650123, 0.572549, 0.964706, 0.835294, 1.2394502031271035, 0.658824, 0.980392, 0.843137, 1.3634516221975588, 0.764706, 0.980392, 0.866667, 1.5109002625955847, 0.827451, 0.980392, 0.886275, 1.848567668998218, 0.913725, 0.988235, 0.937255, 1.9674857522026692, 1.0, 1.0, 0.972549019607843, 2.0940538180126747, 0.988235, 0.980392, 0.870588, 2.295122272133183, 0.992156862745098, 0.972549019607843, 0.803921568627451, 2.4607499453481263, 0.992157, 0.964706, 0.713725, 2.7671612399898713, 0.988235, 0.956863, 0.643137, 3.3362847030303078, 0.980392, 0.917647, 0.509804, 3.906160533501528, 0.968627, 0.87451, 0.407843, 4.590180174288493, 0.94902, 0.823529, 0.321569, 5.161747005977908, 0.929412, 0.776471, 0.278431, 6.132739611881687, 0.909804, 0.717647, 0.235294, 7.153995561002047, 0.890196, 0.658824, 0.196078, 8.118905664857246, 0.878431, 0.619608, 0.168627, 9.703836300710577, 0.870588, 0.54902, 0.156863, 11.598168871277817, 0.85098, 0.47451, 0.145098, 13.862303216803802, 0.831373, 0.411765, 0.133333, 16.56843012093836, 0.811765, 0.345098, 0.113725, 19.802833077526028, 0.788235, 0.266667, 0.0941176, 23.668639396364757, 0.741176, 0.184314, 0.0745098, 28.289108365555993, 0.690196, 0.12549, 0.0627451, 33.81156131184636, 0.619608, 0.0627451, 0.0431373, 39.95157915386262, 0.54902, 0.027451, 0.0705882, 46.26395044628773, 0.470588, 0.0156863, 0.0901961, 54.565114254433915, 0.4, 0.00392157, 0.101961, 68.99999999999999, 0.188235294117647, 0.0, 0.0705882352941176]
imageScalarsGradientLUT.UseLogScale = 1
imageScalarsGradientLUT.ColorSpace = 'Lab'
imageScalarsGradientLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'ImageScalarsGradient'
imageScalarsGradientPWF = GetOpacityTransferFunction('ImageScalarsGradient')
imageScalarsGradientPWF.Points = [0.05508209364378967, 0.0, 0.5, 0.0, 69.0, 1.0, 0.5, 0.0]
imageScalarsGradientPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
threshold2Display.Representation = 'Wireframe'
threshold2Display.ColorArrayName = ['POINTS', 'ImageScalarsGradient']
threshold2Display.LookupTable = imageScalarsGradientLUT
threshold2Display.OSPRayScaleArray = 'ImageScalarsGradient'
threshold2Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold2Display.SelectOrientationVectors = 'ImageScalarsGradient'
threshold2Display.ScaleFactor = 47.6
threshold2Display.SelectScaleArray = 'ImageScalarsGradient'
threshold2Display.GlyphType = 'Arrow'
threshold2Display.GlyphTableIndexArray = 'ImageScalarsGradient'
threshold2Display.GaussianRadius = 2.38
threshold2Display.SetScaleArray = ['POINTS', 'ImageScalarsGradient']
threshold2Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold2Display.OpacityArray = ['POINTS', 'ImageScalarsGradient']
threshold2Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold2Display.DataAxesGrid = 'GridAxesRepresentation'
threshold2Display.PolarAxes = 'PolarAxesRepresentation'
threshold2Display.ScalarOpacityFunction = imageScalarsGradientPWF
threshold2Display.ScalarOpacityUnitDistance = 8.802317034613996

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold2Display.ScaleTransferFunction.Points = [-528.2779358300792, 0.0, 0.5, 0.0, 524.9725535283613, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold2Display.OpacityTransferFunction.Points = [-528.2779358300792, 0.0, 0.5, 0.0, 524.9725535283613, 1.0, 0.5, 0.0]

# show data from threshold3
threshold3Display = Show(threshold3, renderView1)

# trace defaults for the display properties.
threshold3Display.Representation = 'Wireframe'
threshold3Display.ColorArrayName = ['POINTS', 'ImageScalarsGradient']
threshold3Display.LookupTable = imageScalarsGradientLUT
threshold3Display.OSPRayScaleArray = 'ImageScalarsGradient'
threshold3Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold3Display.SelectOrientationVectors = 'ImageScalarsGradient'
threshold3Display.ScaleFactor = 49.900000000000006
threshold3Display.SelectScaleArray = 'ImageScalarsGradient'
threshold3Display.GlyphType = 'Arrow'
threshold3Display.GlyphTableIndexArray = 'ImageScalarsGradient'
threshold3Display.GaussianRadius = 2.495
threshold3Display.SetScaleArray = ['POINTS', 'ImageScalarsGradient']
threshold3Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold3Display.OpacityArray = ['POINTS', 'ImageScalarsGradient']
threshold3Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold3Display.DataAxesGrid = 'GridAxesRepresentation'
threshold3Display.PolarAxes = 'PolarAxesRepresentation'
threshold3Display.ScalarOpacityFunction = imageScalarsGradientPWF
threshold3Display.ScalarOpacityUnitDistance = 3.0727523672358505

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold3Display.ScaleTransferFunction.Points = [-389.31248109641166, 0.0, 0.5, 0.0, 389.64738778885675, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold3Display.OpacityTransferFunction.Points = [-389.31248109641166, 0.0, 0.5, 0.0, 389.64738778885675, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

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
uVWLUTColorBar.Visibility = 0

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

# get color legend/bar for sALTLUT in view renderView1
sALTLUTColorBar = GetScalarBar(sALTLUT, renderView1)
sALTLUTColorBar.Title = 'SALT'
sALTLUTColorBar.ComponentTitle = ''

# set color bar visibility
sALTLUTColorBar.Visibility = 0

# get color transfer function/color map for 'cos_gradz'
cos_gradzLUT = GetColorTransferFunction('cos_gradz')
cos_gradzLUT.RGBPoints = [5.241307388104141e-10, 0.0, 1.0, 1.0, 81.00000000028835, 0.0, 0.0, 1.0, 90.00000000026215, 1.0, 1.0, 1.0, 99.00000000023596, 1.0, 0.0, 0.0, 180.00000000000017, 1.0, 1.0, 0.0]
cos_gradzLUT.ColorSpace = 'RGB'
cos_gradzLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for cos_gradzLUT in view renderView1
cos_gradzLUTColorBar = GetScalarBar(cos_gradzLUT, renderView1)
cos_gradzLUTColorBar.Title = 'cos_gradz'
cos_gradzLUTColorBar.ComponentTitle = ''

# set color bar visibility
cos_gradzLUTColorBar.Visibility = 0

# get color legend/bar for imageScalarsGradientLUT in view renderView1
imageScalarsGradientLUTColorBar = GetScalarBar(imageScalarsGradientLUT, renderView1)
imageScalarsGradientLUTColorBar.Title = 'salt gradient'
imageScalarsGradientLUTColorBar.ComponentTitle = ''

# set color bar visibility
imageScalarsGradientLUTColorBar.Visibility = 1

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

# hide data in view
Hide(glyph1, renderView1)

# hide data in view
Hide(grad_salt, renderView1)

# hide data in view
Hide(grad_temp, renderView1)

# hide data in view
Hide(appendAttributes2, renderView1)

# show color legend
threshold2Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(threshold2, renderView1)

# show color legend
threshold3Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'UVW'
uVWPWF = GetOpacityTransferFunction('UVW')
uVWPWF.Points = [0.0, 0.0, 0.5, 0.0, 1.0863515722882156, 1.0, 0.5, 0.0]
uVWPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'Gradients'
gradientsPWF = GetOpacityTransferFunction('Gradients')
gradientsPWF.Points = [0.0, 0.0, 0.5, 0.0, 1914.9857791636152, 1.0, 0.5, 0.0]
gradientsPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'cos_gradz'
cos_gradzPWF = GetOpacityTransferFunction('cos_gradz')
cos_gradzPWF.Points = [5.241307388104133e-10, 0.0, 0.5, 0.0, 180.00000000000003, 1.0, 0.5, 0.0]
cos_gradzPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(threshold2)
# ----------------------------------------------------------------