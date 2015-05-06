#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Plug-in:      Layer via Copy/Cut
# Version:      1.6
# Date:         09.01.2014
# Copyright:    Dmitry Dubyaga <dmitry.dubyaga@gmail.com>
# Website:      some-gimp-plugins.com
# Tested with:  GIMP 2.8


# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from gimpfu import *

def find_layers_in_group(group, elements):
    num_children, child_ids = pdb.gimp_item_get_children(group)
    for id in child_ids:
        child = gimp.Item.from_id(id)
        if pdb.gimp_item_is_group(child):
            find_layers_in_group(child, elements)
        else:
            elements.append(child)
    return elements

def python_fu_layer_via_copy(image, drawable):
    gimp.context_push()
    image.undo_group_start()

    pdb.gimp_message_get_handler(ERROR_CONSOLE)

    if not pdb.gimp_item_is_layer(drawable):
        pdb.gimp_message("The layer or layer group is not selected.")
        image.undo_group_end()
        gimp.context_pop()
        return
    if pdb.gimp_selection_is_empty(image):
        pdb.gimp_message("The selection is empty.")
        image.undo_group_end()
        gimp.context_pop()
        return

    selection = pdb.gimp_selection_save(image)

    if pdb.gimp_item_is_group(drawable):

        parent = pdb.gimp_item_get_parent(drawable)
        position = pdb.gimp_image_get_item_position(image, drawable)
        group_new = pdb.gimp_layer_copy(drawable, TRUE)
        pdb.gimp_image_insert_layer(image, group_new, parent, position)
        group_new.name = "Group via Copy"

        layers_list = find_layers_in_group(group_new, elements = [])
        for element in layers_list:
            element.add_alpha()
            pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, selection)
            pdb.gimp_image_select_item(image, CHANNEL_OP_INTERSECT, element)
            created_mask = element.create_mask(ADD_SELECTION_MASK)
            element.add_mask(created_mask)
            element.remove_mask(MASK_APPLY)
            selection_bounds = pdb.gimp_selection_bounds(image)
            selection_width = selection_bounds[3] - selection_bounds[1]
            selection_height = selection_bounds[4] - selection_bounds[2]
            element_offset_x, element_offset_y = pdb.gimp_drawable_offsets(element)
            element.resize(
                    selection_width,
                    selection_height,
                    element_offset_x - selection_bounds[1],
                    element_offset_y - selection_bounds[2]
                    )
        image.remove_channel(selection)

        pdb.gimp_selection_none(image)
        pdb.gimp_image_set_active_layer(image, group_new)

        gimp.displays_flush()
        image.undo_group_end()
        gimp.context_pop()
        return

    parent = pdb.gimp_item_get_parent(drawable)
    position = pdb.gimp_image_get_item_position(image, drawable)
    layer_new = pdb.gimp_layer_copy(drawable, TRUE)
    pdb.gimp_image_insert_layer(image, layer_new, parent, position)
    layer_new.name = "Layer via Copy"

    layer_new.add_alpha()
    pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, selection)
    pdb.gimp_image_select_item(image, CHANNEL_OP_INTERSECT, layer_new)
    created_mask = layer_new.create_mask(ADD_SELECTION_MASK)
    layer_new.add_mask(created_mask)
    layer_new.remove_mask(MASK_APPLY)
    selection_bounds = pdb.gimp_selection_bounds(image)
    selection_width = selection_bounds[3] - selection_bounds[1]
    selection_height = selection_bounds[4] - selection_bounds[2]

    layer_offset_x, layer_offset_y = pdb.gimp_drawable_offsets(layer_new)
    layer_new.resize(
            selection_width,
            selection_height,
            layer_offset_x - selection_bounds[1],
            layer_offset_y - selection_bounds[2]
            )
    image.remove_channel(selection)
    pdb.gimp_selection_none(image)

    gimp.displays_flush()
    image.undo_group_end()
    gimp.context_pop()
    return

def python_fu_layer_via_cut(image, drawable):
    gimp.context_push()
    image.undo_group_start()

    pdb.gimp_message_get_handler(ERROR_CONSOLE)

    if not pdb.gimp_item_is_layer(drawable):
        pdb.gimp_message("The layer or layer group is not selected.")
        image.undo_group_end()
        gimp.context_pop()
        return
    if pdb.gimp_selection_is_empty(image):
        pdb.gimp_message("The selection is empty.")
        image.undo_group_end()
        gimp.context_pop()
        return

    selection = pdb.gimp_selection_save(image)

    if pdb.gimp_item_is_group(drawable):

        parent = pdb.gimp_item_get_parent(drawable)
        position = pdb.gimp_image_get_item_position(image, drawable)
        group_new = pdb.gimp_layer_copy(drawable, TRUE)
        pdb.gimp_image_insert_layer(image, group_new, parent, position)
        group_new.name = "Group via Cut"

        layers_list = find_layers_in_group(group_new, elements = [])
        for element in layers_list:
            element.add_alpha()
            pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, selection)
            pdb.gimp_image_select_item(image, CHANNEL_OP_INTERSECT, element)
            created_mask = element.create_mask(ADD_SELECTION_MASK)
            element.add_mask(created_mask)
            element.remove_mask(MASK_APPLY)
            selection_bounds = pdb.gimp_selection_bounds(image)
            selection_width = selection_bounds[3] - selection_bounds[1]
            selection_height = selection_bounds[4] - selection_bounds[2]
            element_offset_x, element_offset_y = pdb.gimp_drawable_offsets(element)
            element.resize(
                    selection_width,
                    selection_height,
                    element_offset_x - selection_bounds[1],
                    element_offset_y - selection_bounds[2]
                    )
        layers_list = find_layers_in_group(drawable, elements = [])
        for element in layers_list:
            element.add_alpha()
            pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, selection)
            pdb.gimp_image_select_item(image, CHANNEL_OP_INTERSECT, element)
            created_mask = element.create_mask(ADD_SELECTION_MASK)
            element.add_mask(created_mask)
            pdb.gimp_selection_none(image)
            pdb.gimp_invert(created_mask)
            element.remove_mask(MASK_APPLY)

        image.remove_channel(selection)
        pdb.gimp_image_set_active_layer(image, group_new)

        gimp.displays_flush()
        image.undo_group_end()
        gimp.context_pop()
        return

    parent = pdb.gimp_item_get_parent(drawable)
    position = pdb.gimp_image_get_item_position(image, drawable)
    layer_new = pdb.gimp_layer_copy(drawable, TRUE)
    pdb.gimp_image_insert_layer(image, layer_new, parent, position)
    layer_new.name = "Layer via Cut"

    layer_new.add_alpha()
    pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, selection)
    pdb.gimp_image_select_item(image, CHANNEL_OP_INTERSECT, layer_new)
    created_mask = layer_new.create_mask(ADD_SELECTION_MASK)
    layer_new.add_mask(created_mask)
    layer_new.remove_mask(MASK_APPLY)
    selection_bounds = pdb.gimp_selection_bounds(image)
    selection_width = selection_bounds[3] - selection_bounds[1]
    selection_height = selection_bounds[4] - selection_bounds[2]
    layer_offset_x, layer_offset_y = pdb.gimp_drawable_offsets(layer_new)
    layer_new.resize(
            selection_width,
            selection_height,
            layer_offset_x - selection_bounds[1],
            layer_offset_y - selection_bounds[2]
            )
    drawable.add_alpha()
    pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, selection)
    pdb.gimp_image_select_item(image, CHANNEL_OP_INTERSECT, drawable)
    created_mask = drawable.create_mask(ADD_SELECTION_MASK)
    drawable.add_mask(created_mask)
    pdb.gimp_selection_none(image)
    pdb.gimp_invert(created_mask)
    drawable.remove_mask(MASK_APPLY)

    image.remove_channel(selection)

    gimp.displays_flush()
    image.undo_group_end()
    gimp.context_pop()
    return

register (
    "python-fu-layer-via-copy",
    "Copy and move the selected area to a new layer in the same position.",
    "Copy and move the selected area to a new layer in the same position.",
    "Dmirty Dubyaga",
    "Dmitry Dubyaga <dmitry.dubyaga@gmail.com>",
    "09.01.2014",
    "Layer via Copy",
    "*",
    [
        (PF_IMAGE, "image", "", None),
        (PF_DRAWABLE, "drawable", "", None)
    ],
    [],
    python_fu_layer_via_copy, menu="<Image>/Layer/"
    )
register (
    "python-fu-layer-via-cut",
    "Cut and move the selected area to a new layer in the same position.",
    "Cut and move the selected area to a new layer in the same position.",
    "Dmirty Dubyaga",
    "Dmitry Dubyaga <dmitry.dubyaga@gmail.com>",
    "09.01.2014",
    "Layer via Cut",
    "*",
    [
        (PF_IMAGE, "image", "", None),
        (PF_DRAWABLE, "drawable", "", None)
    ],
    [],
    python_fu_layer_via_cut, menu="<Image>/Layer/"
    )

main()
