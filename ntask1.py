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
renderView1.CameraParallelScale = 17.357897016652466
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
netCDFReader2 = NetCDFReader(FileName=['/home/intel_lab3/Documents/GAVNitish/0001/COMBINED_2011013100.nc'])
netCDFReader2.Dimensions = '(Z_MIT40, YC, XC)'
netCDFReader2.SphericalCoordinates = 0

# create a new 'XDMF Reader'
xDMFReader1 = XDMFReader(FileNames=['/home/intel_lab3/Documents/GAVNitish/0001/bathymetry.xmf'])
xDMFReader1.PointArrayStatus = ['depth']
xDMFReader1.GridStatus = ['Grid']

# create a new 'Resample To Image'
resampleToImage2 = ResampleToImage(Input=netCDFReader2)
resampleToImage2.UseInputBounds = 0
resampleToImage2.SamplingDimensions = [500, 500, 50]
resampleToImage2.SamplingBounds = [30.027099609375, 49.987098693847656, 10.027099609375, 29.98710060119629, -3178.0, -2.0]

# create a new 'NetCDF Reader'
netCDFReader3 = NetCDFReader(FileName=['/home/intel_lab3/Documents/GAVNitish/0001/COMBINED_2011013100.nc'])
netCDFReader3.Dimensions = '(Z_MIT40, YG, XC)'
netCDFReader3.SphericalCoordinates = 0

# create a new 'Resample To Image'
resampleToImage3 = ResampleToImage(Input=netCDFReader3)
resampleToImage3.UseInputBounds = 0
resampleToImage3.SamplingDimensions = [500, 500, 50]
resampleToImage3.SamplingBounds = [30.027099609375, 49.987098693847656, 10.007100105285645, 29.967100143432617, -3178.0, -2.0]

# create a new 'NetCDF Reader'
netCDFReader1 = NetCDFReader(FileName=['/home/intel_lab3/Documents/GAVNitish/0001/COMBINED_2011013100.nc'])
netCDFReader1.Dimensions = '(Z_MIT40, YC, XG)'
netCDFReader1.SphericalCoordinates = 0

# create a new 'Resample To Image'
resampleToImage1 = ResampleToImage(Input=netCDFReader1)
resampleToImage1.UseInputBounds = 0
resampleToImage1.SamplingDimensions = [500, 500, 50]
resampleToImage1.SamplingBounds = [30.007099151611328, 49.967098236083984, 10.027099609375, 29.98710060119629, -3178.0, -2.0]

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

# create a new 'Gradient Of Unstructured DataSet'
gradient_temp = GradientOfUnstructuredDataSet(Input=transform1)
gradient_temp.ScalarArray = ['POINTS', 'TEMP']

# create a new 'Contour'
contour2 = Contour(Input=gradient_temp)
contour2.ContourBy = ['POINTS', 'TEMP']
contour2.ComputeGradients = 1
contour2.Isosurfaces = [0.0, 0.0, 3.4635321770352903, 6.9270643540705805, 10.39059653110587, 13.854128708141161, 17.31766088517645, 20.78119306221174, 24.244725239247032, 27.708257416282322, 31.171789593317612]
contour2.PointMergeMethod = 'Uniform Binning'

# create a new 'Warp By Scalar'
warpByScalar1 = WarpByScalar(Input=xDMFReader1)
warpByScalar1.Scalars = ['POINTS', '']
warpByScalar1.ScaleFactor = 0.00025

# create a new 'Threshold'
threshold1 = Threshold(Input=warpByScalar1)
threshold1.Scalars = ['POINTS', '']
threshold1.ThresholdRange = [-3073.121826171875, -0.0]

# create a new 'Calculator'
calculator4 = Calculator(Input=contour2)
calculator4.ResultArrayName = 'temp_grad'
calculator4.Function = 'gradient_temp_X^2+gradient_temp_Y^2+gradient_temp_Z^2'

# create a new 'Gradient Of Unstructured DataSet'
gradient_salt = GradientOfUnstructuredDataSet(Input=transform1)
gradient_salt.ScalarArray = ['POINTS', 'SALT']

# create a new 'Contour'
contour1 = Contour(Input=gradient_salt)
contour1.ContourBy = ['POINTS', 'SALT']
contour1.ComputeGradients = 1
contour1.Isosurfaces = [0.0, 4.716596927179654, 9.433193854359308, 14.149790781538963, 18.866387708718616, 23.582984635898274, 28.299581563077925, 33.01617849025758, 37.73277541743723, 42.44937234461689]
contour1.PointMergeMethod = 'Uniform Binning'

# create a new 'Calculator'
calculator3 = Calculator(Input=contour1)
calculator3.ResultArrayName = 'salt_grad'
calculator3.Function = 'gradient_salt_X^2+gradient_salt_Y^2+gradient_salt_Z^2'

# create a new 'Threshold'
threshold2 = Threshold(Input=calculator3)
threshold2.Scalars = ['POINTS', 'SALT']
threshold2.ThresholdRange = [4.716597080230713, 35.28014422893524]

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

# show data from gradient_salt
gradient_saltDisplay = Show(gradient_salt, renderView1)

# trace defaults for the display properties.
gradient_saltDisplay.Representation = 'Outline'
gradient_saltDisplay.ColorArrayName = [None, '']
gradient_saltDisplay.OSPRayScaleArray = 'Gradients'
gradient_saltDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
gradient_saltDisplay.SelectOrientationVectors = 'Speed'
gradient_saltDisplay.ScaleFactor = 1.996000099182129
gradient_saltDisplay.SelectScaleArray = 'Gradients'
gradient_saltDisplay.GlyphType = 'Arrow'
gradient_saltDisplay.GlyphTableIndexArray = 'Gradients'
gradient_saltDisplay.GaussianRadius = 0.09980000495910644
gradient_saltDisplay.SetScaleArray = ['POINTS', 'Gradients']
gradient_saltDisplay.ScaleTransferFunction = 'PiecewiseFunction'
gradient_saltDisplay.OpacityArray = ['POINTS', 'Gradients']
gradient_saltDisplay.OpacityTransferFunction = 'PiecewiseFunction'
gradient_saltDisplay.DataAxesGrid = 'GridAxesRepresentation'
gradient_saltDisplay.PolarAxes = 'PolarAxesRepresentation'
gradient_saltDisplay.ScalarOpacityUnitDistance = 0.12266336815460342

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
gradient_saltDisplay.ScaleTransferFunction.Points = [-528.2779358300936, 0.0, 0.5, 0.0, 530.6171786461291, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
gradient_saltDisplay.OpacityTransferFunction.Points = [-528.2779358300936, 0.0, 0.5, 0.0, 530.6171786461291, 1.0, 0.5, 0.0]

# show data from contour1
contour1Display = Show(contour1, renderView1)

# get color transfer function/color map for 'Gradients'
gradientsLUT = GetColorTransferFunction('Gradients')
gradientsLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 1281.0623890171023, 0.865003, 0.865003, 0.865003, 2562.1247780342046, 0.705882, 0.0156863, 0.14902]
gradientsLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = ['POINTS', 'Gradients']
contour1Display.LookupTable = gradientsLUT
contour1Display.OSPRayScaleArray = 'SALT'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'Gradients'
contour1Display.ScaleFactor = 1.9115710479371786
contour1Display.SelectScaleArray = 'SALT'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'SALT'
contour1Display.GaussianRadius = 0.09557855239685893
contour1Display.SetScaleArray = ['POINTS', 'SALT']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = ['POINTS', 'SALT']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display.ScaleTransferFunction.Points = [21.224685668945312, 0.0, 0.5, 0.0, 21.228591918945312, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display.OpacityTransferFunction.Points = [21.224685668945312, 0.0, 0.5, 0.0, 21.228591918945312, 1.0, 0.5, 0.0]

# show data from calculator3
calculator3Display = Show(calculator3, renderView1)

# trace defaults for the display properties.
calculator3Display.Representation = 'Surface'
calculator3Display.ColorArrayName = ['POINTS', 'Gradients']
calculator3Display.LookupTable = gradientsLUT
calculator3Display.OSPRayScaleArray = 'SALT'
calculator3Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator3Display.SelectOrientationVectors = 'Gradients'
calculator3Display.ScaleFactor = 1.9115710479371786
calculator3Display.SelectScaleArray = 'SALT'
calculator3Display.GlyphType = 'Arrow'
calculator3Display.GlyphTableIndexArray = 'SALT'
calculator3Display.GaussianRadius = 0.09557855239685893
calculator3Display.SetScaleArray = ['POINTS', 'SALT']
calculator3Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator3Display.OpacityArray = ['POINTS', 'SALT']
calculator3Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator3Display.DataAxesGrid = 'GridAxesRepresentation'
calculator3Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator3Display.ScaleTransferFunction.Points = [21.224685668945312, 0.0, 0.5, 0.0, 21.228591918945312, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator3Display.OpacityTransferFunction.Points = [21.224685668945312, 0.0, 0.5, 0.0, 21.228591918945312, 1.0, 0.5, 0.0]

# show data from gradient_temp
gradient_tempDisplay = Show(gradient_temp, renderView1)

# trace defaults for the display properties.
gradient_tempDisplay.Representation = 'Outline'
gradient_tempDisplay.ColorArrayName = [None, '']
gradient_tempDisplay.OSPRayScaleArray = 'Gradients'
gradient_tempDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
gradient_tempDisplay.SelectOrientationVectors = 'Speed'
gradient_tempDisplay.ScaleFactor = 1.996000099182129
gradient_tempDisplay.SelectScaleArray = 'Gradients'
gradient_tempDisplay.GlyphType = 'Arrow'
gradient_tempDisplay.GlyphTableIndexArray = 'Gradients'
gradient_tempDisplay.GaussianRadius = 0.09980000495910644
gradient_tempDisplay.SetScaleArray = ['POINTS', 'Gradients']
gradient_tempDisplay.ScaleTransferFunction = 'PiecewiseFunction'
gradient_tempDisplay.OpacityArray = ['POINTS', 'Gradients']
gradient_tempDisplay.OpacityTransferFunction = 'PiecewiseFunction'
gradient_tempDisplay.DataAxesGrid = 'GridAxesRepresentation'
gradient_tempDisplay.PolarAxes = 'PolarAxesRepresentation'
gradient_tempDisplay.ScalarOpacityUnitDistance = 0.12266336815460342

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
gradient_tempDisplay.ScaleTransferFunction.Points = [-389.31248109642223, 0.0, 0.5, 0.0, 389.6473877888673, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
gradient_tempDisplay.OpacityTransferFunction.Points = [-389.31248109642223, 0.0, 0.5, 0.0, 389.6473877888673, 1.0, 0.5, 0.0]

# show data from contour2
contour2Display = Show(contour2, renderView1)

# get color transfer function/color map for 'TEMP'
tEMPLUT = GetColorTransferFunction('TEMP')
tEMPLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 15.585894584655762, 0.865003, 0.865003, 0.865003, 31.171789169311523, 0.705882, 0.0156863, 0.14902]
tEMPLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
contour2Display.Representation = 'Surface'
contour2Display.ColorArrayName = ['POINTS', 'TEMP']
contour2Display.LookupTable = tEMPLUT
contour2Display.OSPRayScaleArray = 'TEMP'
contour2Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour2Display.SelectOrientationVectors = 'Gradients'
contour2Display.ScaleFactor = 1.909399295082281
contour2Display.SelectScaleArray = 'TEMP'
contour2Display.GlyphType = 'Arrow'
contour2Display.GlyphTableIndexArray = 'TEMP'
contour2Display.GaussianRadius = 0.09546996475411405
contour2Display.SetScaleArray = ['POINTS', 'TEMP']
contour2Display.ScaleTransferFunction = 'PiecewiseFunction'
contour2Display.OpacityArray = ['POINTS', 'TEMP']
contour2Display.OpacityTransferFunction = 'PiecewiseFunction'
contour2Display.DataAxesGrid = 'GridAxesRepresentation'
contour2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour2Display.ScaleTransferFunction.Points = [21.224685668945312, 0.0, 0.5, 0.0, 21.228591918945312, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour2Display.OpacityTransferFunction.Points = [21.224685668945312, 0.0, 0.5, 0.0, 21.228591918945312, 1.0, 0.5, 0.0]

# show data from calculator4
calculator4Display = Show(calculator4, renderView1)

# trace defaults for the display properties.
calculator4Display.Representation = 'Surface'
calculator4Display.ColorArrayName = ['POINTS', 'TEMP']
calculator4Display.LookupTable = tEMPLUT
calculator4Display.OSPRayScaleArray = 'TEMP'
calculator4Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator4Display.SelectOrientationVectors = 'Gradients'
calculator4Display.ScaleFactor = 1.909399295082281
calculator4Display.SelectScaleArray = 'TEMP'
calculator4Display.GlyphType = 'Arrow'
calculator4Display.GlyphTableIndexArray = 'TEMP'
calculator4Display.GaussianRadius = 0.09546996475411405
calculator4Display.SetScaleArray = ['POINTS', 'TEMP']
calculator4Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator4Display.OpacityArray = ['POINTS', 'TEMP']
calculator4Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator4Display.DataAxesGrid = 'GridAxesRepresentation'
calculator4Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator4Display.ScaleTransferFunction.Points = [21.224685668945312, 0.0, 0.5, 0.0, 21.228591918945312, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator4Display.OpacityTransferFunction.Points = [21.224685668945312, 0.0, 0.5, 0.0, 21.228591918945312, 1.0, 0.5, 0.0]

# show data from threshold2
threshold2Display = Show(threshold2, renderView1)

# get opacity transfer function/opacity map for 'TEMP'
tEMPPWF = GetOpacityTransferFunction('TEMP')
tEMPPWF.Points = [0.0, 0.0, 0.5, 0.0, 8.731856346130371, 0.29411765933036804, 0.5, 0.0, 13.23862075805664, 0.5220588445663452, 0.5, 0.0, 31.171789169311523, 1.0, 0.5, 0.0]
tEMPPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
threshold2Display.Representation = 'Surface'
threshold2Display.ColorArrayName = ['POINTS', 'TEMP']
threshold2Display.LookupTable = tEMPLUT
threshold2Display.OSPRayScaleArray = 'SALT'
threshold2Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold2Display.SelectOrientationVectors = 'Gradients'
threshold2Display.ScaleFactor = 1.9150158905747874
threshold2Display.SelectScaleArray = 'SALT'
threshold2Display.GlyphType = 'Arrow'
threshold2Display.GlyphTableIndexArray = 'SALT'
threshold2Display.GaussianRadius = 0.09575079452873936
threshold2Display.SetScaleArray = ['POINTS', 'SALT']
threshold2Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold2Display.OpacityArray = ['POINTS', 'SALT']
threshold2Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold2Display.DataAxesGrid = 'GridAxesRepresentation'
threshold2Display.PolarAxes = 'PolarAxesRepresentation'
threshold2Display.ScalarOpacityFunction = tEMPPWF
threshold2Display.ScalarOpacityUnitDistance = 0.22700597051651872

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold2Display.ScaleTransferFunction.Points = [4.716597080230713, 0.0, 0.5, 0.0, 37.7327766418457, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold2Display.OpacityTransferFunction.Points = [4.716597080230713, 0.0, 0.5, 0.0, 37.7327766418457, 1.0, 0.5, 0.0]

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
uVWLUTColorBar.Visibility = 1

# get color legend/bar for gradientsLUT in view renderView1
gradientsLUTColorBar = GetScalarBar(gradientsLUT, renderView1)
gradientsLUTColorBar.WindowLocation = 'UpperLeftCorner'
gradientsLUTColorBar.Position = [0.9246753246753247, 0.01509433962264151]
gradientsLUTColorBar.Title = 'Gradients'
gradientsLUTColorBar.ComponentTitle = 'Magnitude'

# set color bar visibility
gradientsLUTColorBar.Visibility = 0

# get color transfer function/color map for 'SALT'
sALTLUT = GetColorTransferFunction('SALT')
sALTLUT.RGBPoints = [4.716597080230713, 0.231373, 0.298039, 0.752941, 21.224686861038208, 0.865003, 0.865003, 0.865003, 37.7327766418457, 0.705882, 0.0156863, 0.14902]
sALTLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for sALTLUT in view renderView1
sALTLUTColorBar = GetScalarBar(sALTLUT, renderView1)
sALTLUTColorBar.Position = [0.9203843514070007, 0.01509433962264151]
sALTLUTColorBar.Title = 'SALT'
sALTLUTColorBar.ComponentTitle = ''

# set color bar visibility
sALTLUTColorBar.Visibility = 0

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

# hide data in view
Hide(gradient_salt, renderView1)

# hide data in view
Hide(contour1, renderView1)

# hide data in view
Hide(calculator3, renderView1)

# hide data in view
Hide(gradient_temp, renderView1)

# hide data in view
Hide(contour2, renderView1)

# hide data in view
Hide(calculator4, renderView1)

# hide data in view
Hide(threshold2, renderView1)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'SALT'
sALTPWF = GetOpacityTransferFunction('SALT')
sALTPWF.Points = [4.716597080230713, 0.0, 0.5, 0.0, 37.7327766418457, 1.0, 0.5, 0.0]
sALTPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'Gradients'
gradientsPWF = GetOpacityTransferFunction('Gradients')
gradientsPWF.Points = [0.0, 0.0, 0.5, 0.0, 2562.1247780342046, 1.0, 0.5, 0.0]
gradientsPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'UVW'
uVWPWF = GetOpacityTransferFunction('UVW')
uVWPWF.Points = [0.0, 0.0, 0.5, 0.0, 1.0863515722882156, 1.0, 0.5, 0.0]
uVWPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(glyph1)
# ----------------------------------------------------------------