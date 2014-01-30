# Automatically generated code: EDIT AT YOUR OWN RISK
from traits import api as traits
from traitsui import api as traitsui

from tvtk import vtk_module as vtk
from tvtk import tvtk_base
from tvtk.tvtk_base_handler import TVTKBaseHandler
from tvtk import messenger
from tvtk.tvtk_base import deref_vtk
from tvtk import array_handler
from tvtk.array_handler import deref_array
from tvtk.tvtk_classes.tvtk_helper import wrap_vtk

from tvtk.tvtk_classes.volume_texture_mapper import VolumeTextureMapper


class VolumeTextureMapper2D(VolumeTextureMapper):
    """
    VolumeTextureMapper2D - Abstract class for a volume mapper
    
    Superclass: VolumeTextureMapper
    
    VolumeTextureMapper2D renders a volume using 2d texture mapping.
    
    See Also:
    
    VolumeMapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVolumeTextureMapper2D, obj, update, **traits)
    
    target_texture_size = traits.Array(shape=(2,), value=(512, 512), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _target_texture_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTargetTextureSize,
                        self.target_texture_size)

    maximum_storage_size = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        This is the maximum size of saved textures in bytes. If this size
        is large enough to hold the RGBA textures for all three
        directions (_xx_yx_zx3x4 is the approximate value - it is actually a
        bit larger due to wasted space in the textures) then the textures
        will be saved.
        """
    )
    def _maximum_storage_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumStorageSize,
                        self.maximum_storage_size)

    maximum_number_of_planes = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        This is the maximum number of planes that will be created for
        texture mapping the volume. If the volume has more voxels than
        this along the viewing direction, then planes of the volume will
        be skipped to ensure that this maximum is not violated. A skip
        factor is used, and is incremented until the maximum condition is
        satisfied.
        """
    )
    def _maximum_number_of_planes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumNumberOfPlanes,
                        self.maximum_number_of_planes)

    def _get_internal_skip_factor(self):
        return self._vtk_obj.GetInternalSkipFactor()
    internal_skip_factor = traits.Property(_get_internal_skip_factor, help=\
        """
        Made public only for access from the templated method. Not a
        GetMacro to avoid the print_self defect.
        """
    )

    def _get_save_textures(self):
        return self._vtk_obj.GetSaveTextures()
    save_textures = traits.Property(_get_save_textures, help=\
        """
        
        """
    )

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('target_texture_size', 'GetTargetTextureSize'),
    ('maximum_storage_size', 'GetMaximumStorageSize'), ('progress_text',
    'GetProgressText'), ('maximum_number_of_planes',
    'GetMaximumNumberOfPlanes'), ('debug', 'GetDebug'),
    ('cropping_region_planes', 'GetCroppingRegionPlanes'),
    ('cropping_region_flags', 'GetCroppingRegionFlags'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('scalar_mode',
    'GetScalarMode'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('cropping', 'GetCropping'),
    ('abort_execute', 'GetAbortExecute'), ('blend_mode', 'GetBlendMode'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'cropping', 'debug', 'global_warning_display',
    'release_data_flag', 'blend_mode', 'cropping_region_flags',
    'scalar_mode', 'cropping_region_planes', 'maximum_number_of_planes',
    'maximum_storage_size', 'progress_text', 'target_texture_size'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VolumeTextureMapper2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit VolumeTextureMapper2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['cropping'], ['blend_mode', 'cropping_region_flags',
            'scalar_mode'], ['cropping_region_planes', 'maximum_number_of_planes',
            'maximum_storage_size', 'target_texture_size']),
            title='Edit VolumeTextureMapper2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VolumeTextureMapper2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            
