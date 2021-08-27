# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ParcelleInfos
                                 A QGIS plugin
 Déterminer les parcelles susceptibles d'accueillir des projets de dérogation
                             -------------------
        begin                : 2018-07-08
        copyright            : (C) 2018 by EL AYEDI achraf
        email                : achrafelayediz@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ParcelleInfos class from file ParcelleInfos.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .parcelle_infos import ParcelleInfos
    return ParcelleInfos(iface)
