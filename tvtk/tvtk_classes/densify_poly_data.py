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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class DensifyPolyData(PolyDataAlgorithm):
    """
    DensifyPolyData - Densify the input by adding points at the
    
    Superclass: PolyDataAlgorithm
    
    The filter takes any polygonal data as input and will tessellate
    cells that are planar polygons present by fanning out triangles from
    its centroid. Other cells are simply passed through to the output. 
    point_data, if present, is interpolated via linear interpolation.
    cell_data for any tessellated cell is simply copied over from its
    parent cell. Planar polygons are assumed to be convex. Funny things
    will happen if they are not.
    
    The number of subdivisions can be controlled by the parameter
    number_of_subdivisions.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDensifyPolyData, obj, update, **traits)
    
    number_of_subdivisions = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Number of recursive subdivisions. Initial value is 1.
        """
    )
    def _number_of_subdivisions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfSubdivisions,
                        self.number_of_subdivisions)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('number_of_subdivisions',
    'GetNumberOfSubdivisions'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'number_of_subdivisions', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DensifyPolyData, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DensifyPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['number_of_subdivisions']),
            title='Edit DensifyPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DensifyPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            
