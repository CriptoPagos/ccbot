#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Cryptocurrency bot (ccbot)
Copyright (C) SASCO SpA (https://sasco.cl)

Este programa es software libre: usted puede redistribuirlo y/o
modificarlo bajo los términos de la Licencia Pública General Affero de GNU
publicada por la Fundación para el Software Libre, ya sea la versión
3 de la Licencia, o (a su elección) cualquier versión posterior de la
misma.

Este programa se distribuye con la esperanza de que sea útil, pero
SIN GARANTÍA ALGUNA; ni siquiera la garantía implícita
MERCANTIL o de APTITUD PARA UN PROPÓSITO DETERMINADO.
Consulte los detalles de la Licencia Pública General Affero de GNU para
obtener una información más detallada.

Debería haber recibido una copia de la Licencia Pública General Affero de GNU
junto a este programa.
En caso contrario, consulte <http://www.gnu.org/licenses/agpl.html>.
"""

"""
@file bot.py Lanzador del bot: crea el bot y lo inicializa con la configuración
@author Esteban De La Fuente Rubio, DeLaF (esteban[at]sasco.cl)
@version 2017-11-29
"""

# importar módulos
import sys
from ccbot import Bot

# crear y lanzar bot con la configuración pasada como parámetro o la por defecto
try :
    config = sys.argv[1] if len(sys.argv) == 2 else 'config.yml'
    Bot = Bot(config)
    rc = Bot.start()
    sys.exit(rc)
except Exception as e:
    print(e)
    sys.exit(1)
