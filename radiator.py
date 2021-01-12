#!/usr/bin/python

import math
from argparse import ArgumentParser

class Material:

	def __init__ (self, heat_capacity, conductivity):

		self . heat_capacity = heat_capacity
		self . conductivity = conductivity



class Pipe:

	def __init__ (self, material):

		self . conductivity = material . conductivity
		self . thermal_mass = 100000 * material . heat_capacity / 5



class RadiantPipe:

	def __init__ (self, material):

		self . conductivity = material . conductivity * 2
		self . thermal_mass = 50000 * material . heat_capacity / 5



class Coolant:

	def __init__ (self, material, mass):

		self . conductivity = material . conductivity
		self . thermal_mass = mass * material . heat_capacity



class MineralTile:

	def __init__ (self, material):

		self . conductivity = material . conductivity
		self . thermal_mass = 200000 * material . heat_capacity



class ManufacturedTile:

	def __init__ (self, material):

		self . conductivity = material .conductivity
		self . thermal_mass = 100000 * material . heat_capacity


class Door:

	def __init__ (self, material):

		self . conductivity = material . conductivity
		self . thermal_mass = 400000 * material . heat_capacity



materials = {
	"Abyssalite": Material (4, 0),
	"Algea": Material (0.2, 2),
	"Aluminum Gas": Material (0.91, 2.5),
	"Molten Aluminum": Material (0.91, 20.5),
	"Aluminum": Material (0.91, 205),
	"Aluminum Ore": Material (0.91, 10.5),
	"Bitumen": Material (1.76, 0.17),
	"Bleach Stone": Material (0.5, 4),
	"Brine": Material (3.4, 0.609),
	"Brine Ice": Material (3.4, 2.18),
	"Ceramic": Material (0.84, 0.62),
	"Carbon Gas": Material (0.71, 1.7),
	"Molten Carbon": Material (0.71, 2),
	"Refined Carbon": Material (1.74, 3.1),
	"Carbon Dioxide": Material (0.846, 0.015),
	"Liquid Carbon Dioxide": Material (0.846, 1.46),
	"Solid Carbon Dioxide": Material (0.846, 1.46),
	"Chlorine": Material (0.480, 0.008),
	"Liquid Chlorine": Material (0.48, 0.008),
	"Solid Chlorine": Material (0.48, 0.75),
	"Clay": Material (0.92, 2),
	"Coal": Material (0.71, 1.25),
	"Cobalt Gas": Material (0.42, 1),
	"Molten Colbalt": Material (0.42, 4),
	"Cobalt": Material (0.42, 100),
	"Cobalt Ore": Material (0.42, 4),
	"Copper Gas": Material (0.386, 1),
	"Molten Copper": Material (0.386, 12),
	"Copper": Material (0.385, 60),
	"Copper Ore": Material (0.386, 4.5),
	"Corium": Material (7.44, 6),
	"Crude Oil": Material (1.69, 2),
	"Frozen Crude Oil": Material (1.69, 2),
	"Crushed Ice": Material (2.05, 2.18),
	"Crushed Rock": Material (0.2, 2),
	"Depleted Uranium": Material (1, 20),
	"Diamond": Material (0.516, 80),
	"Dirt": Material (1.48, 2),
	"Electrum": Material (0.15, 2),
	"Enriched Uranium": Material (1, 20),
	"Ethanol": Material (2.148, 0.167),
	"Frozen Ethanol": Material (2.46, 20),
	"Fertilizer": Material (0.83, 2),
	"Fossil": Material (0.91, 2),
	"Fullerine": Material (0.95, 50),
	"Glass": Material (0.84, 1.11),
	"Molten Glass": Material (0.2, 1),
	"Gold Gas": Material (0.129, 1),
	"Molten Gold": Material (0.129, 6),
	"Gold": Material (0.129, 60),
	"Gold Amalgam": Material (0.15, 2),
	"Granite": Material (0.79, 3.39),
	"Hydrogen": Material (2.4, 0.168),
	"Liquid Hydrogen": Material (2.4, 0.1),
	"Solid Hydrogen": Material (2.4, 1),
	"Ice": Material (2.05, 2.180),
	"Igneous Rock": Material (1, 2),
	"Insulation": Material (5.57, 0),
	"Iron Gas": Material (0.449, 1),
	"Molten Iron": Material (0.449, 4),
	"Iron": Material (0.449, 55),
	"Iron Ore": Material (0.449, 4),
	"Isoresin": Material (1.3, 0.17),
	"Lead Gas": Material (0.128, 3.5),
	"Molten Lead": Material (0.128, 11),
	"Lead": Material (0.128, 35),
	"Lime": Material (0.834, 2),
	"Mafic Rock": Material (0.2, 1),
	"Magma": Material (1, 1),
	"Methane": Material (2.191, 0.03),
	"Frozen Methane": Material (2.191, 0.03),
	"Mud": Material (0.83, 2),
	"Naptha": Material (2.191, 0.2),
	"Frozen Naptha": Material (2.191, 0.2),
	"Neutronium": Material (0, 0),
	"Natural Gas": Material (2.191, 0.035),
	"Niobium Gas": Material (0.265, 1),
	"Molten Niobium": Material (0.265, 54),
	"Niobium": Material (0.265, 54),
	"Nuclear Fallout": Material (0.265, 1),
	"Nuclear Waste": Material (7.44, 6),
	"Obsidian": Material (0.2, 2),
	"Oxygen": Material (1.005, 0.024),
	"Liquid Oxygen": Material (1.01, 2),
	"Solid Oxygen": Material (1.01, 1),
	"Oxylite": Material (1, 4),
	"Petroleum": Material (1.76, 2),
	"Frozen Petroleum": Material (1.76, 2),
	"Phosphorite": Material (0.15, 2),
	"Phosphorus Gas": Material (0.77, 0.236),
	"Molten Phosphorus": Material (0.77, 0.236),
	"Phosphorus": Material (0.77, 0.236),
	"Plastic": Material (1.92, 0.15),
	"Polluted Dirt": Material (0.83, 2),
	"Polluted Ice": Material (2.05, 1),
	"Polluted Mud": Material (0.83, 2),
	"Polluted Oxygen": Material (1.01, 0.024),
	"Polluted Water": Material (4.179, 0.58),
	"Pyrite": Material (0.386, 4.5),
	"Radium": Material (1, 20),
	"Regolith": Material (0.2, 1),
	"Rock Gas": Material (1, 0.1),
	"Rust": Material (0.449, 4),
	"Salt Gas": Material (0.88, 0.444),
	"Molten Salt": Material (0.7, 0.444),
	"Salt": Material (0.7, 0.444),
	"Salt Water": Material (4.1, 0.609),
	"Sand": Material (0.83, 2),
	"Sandstone": Material (0.8, 2.9),
	"Sedimentary Rock": Material (0.2, 2),
	"Slime": Material (0.2, 2),
	"Snow": Material (2.05, 0.545),
	"Sour Gas": Material (1.898, 0.018),
	"Steam": Material (4.179, 0.184),
	"Steel Gas": Material (0.49, 1),
	"Molten Steel": Material (0.386, 80),
	"Steel": Material (0.49, 54),
	"Molten Sucrose": Material (0.7, 0.444),
	"Sucrose": Material (0.43, 0.444),
	"Sulfur Gas": Material (0.7, 0.2),
	"Molten Sulfur": Material (0.7, 0.2),
	"Sulfur": Material (0.7, 0.2),
	"Super Coolant Gas": Material (8.44, 1.2),
	"Super Coolant": Material (8.44, 9.46),
	"Frozen Super Coolant": Material (8.44, 9.46),
	"Thermium": Material (0.622, 220),
	"Tungsten Gas": Material (0.134, 1),
	"Molten Tungsten": Material (0.134, 4),
	"Tungsten": Material (0.134, 60),
	"Uranium": Material (1.69, 2),
	"Uranium Ore": Material (1, 20),
	"Visco-Gel": Material (1.55, 0.45),
	"Frozen Visco-Gel": Material (1.55, 0.45),
	"Water": Material (4.179, 0.609),
	"Wolframite": Material (0.134, 15),
}

def isMetal (material_name):

	return material_name in {
		'Aluminum',
		'Cobalt',
		'Copper',
		'Gold',
		'Iron',
		'Lead',
		'Niobium',
		'Steel',
		'Thermium',
		'Tungsten'
	}


def isRawMineral (material_name):

	return material_name in {
		'Abyssalite',
		'Ceramic',
		'Granite',
		'Igneous Rock',
		'Isoresin',
		'Obsidian',
		'Sandstone',
		'Sedimentary Rock'
	}


def isTransparent (material_name):

	return material_name in {
		'Glass',
		'Diamond'
	}


def isInsulator (material_name):

	return material_name in {
		'Ceramic',
		'Insulation'
	}


def pipeFromMaterialName (material_name):

	if isRawMineral (material_name) \
		or isInsulator (material_name) \
		or material_name == 'Wolframite':

		return Pipe (materials [material_name])

	elif isMetal (material_name):

		return RadiantPipe (materials [material_name])

	else:

		return None


def tileFromMaterialName (material_name):

	if isRawMineral (material_name) or isInsulator (material_name):

		return MineralTile (materials [material_name])

	elif isMetal (material_name) \
		or isTransparent (material_name) \
		or material_name == 'Plastic':

		return ManufacturedTile (materials [material_name])

	else:

		return None


def kFromComponents (
	main_coolant,
	main_pipe,
	main_tile,
	door,
	local_tile,
	local_pipe,
	local_coolant,
	cooling
):

	k_main_coolant_to_main_pipe = \
		(main_coolant . conductivity + main_pipe . conductivity) * 25

	if (cooling):

		k_main_pipe_to_main_tile = \
			main_pipe . conductivity \
				* main_tile . conductivity \
				* main_tile . thermal_mass \
				* 0.5
		k_main_pipe_to_door = \
			main_pipe . conductivity \
				* door . conductivity \
				* door . thermal_mass \
				* 0.5

	else:

		k_main_pipe_to_main_tile = \
			main_pipe . conductivity \
				* main_tile . conductivity \
				* main_pipe . thermal_mass \
				* 0.5
		k_main_pipe_to_door = \
			main_pipe . conductivity \
				* door . conductivity \
				* main_pipe . thermal_mass \
				* 0.5

	k_main_tile_to_door = \
		math.sqrt (main_tile . conductivity * door . conductivity) * 1000

	k_door_to_local_tile = \
		math.sqrt (door . conductivity * local_tile . conductivity) * 1000

	if (cooling):

		k_door_to_local_pipe = \
			door . conductivity \
				* local_pipe . conductivity \
				* local_pipe . thermal_mass \
				* 0.5
		k_local_tile_to_local_pipe = \
			local_tile . conductivity \
				* local_pipe . conductivity \
				* local_pipe . thermal_mass \
				* 0.5

	else:

		k_door_to_local_pipe = \
			door . conductivity \
				* local_pipe . conductivity \
				* door . thermal_mass \
				* 0.5
		k_local_tile_to_local_pipe = \
			local_tile . conductivity \
				* local_pipe . conductivity \
				* local_tile . thermal_mass \
				* 0.5

	k_local_pipe_to_local_coolant = \
		(local_pipe . conductivity + local_coolant . conductivity) * 25

	# Start computing aggregate values

	r_main_coolant_to_main_tile_to_door = \
		(1 / k_main_coolant_to_main_pipe) \
			+ (1 / k_main_pipe_to_main_tile) \
			+ (1 / k_main_tile_to_door)
	r_main_coolant_to_door = \
		(1 / k_main_coolant_to_main_pipe) + (1 / k_main_pipe_to_door)
	r_all_main_coolant_to_door = \
		1 / (
			(1 / r_main_coolant_to_main_tile_to_door)
			+ (1 / r_main_coolant_to_door)
		)
	r_door_to_local_tile_to_local_coolant = \
		(1 / k_door_to_local_tile) \
			+ (1 / k_local_tile_to_local_pipe) \
			+ (1 / k_local_pipe_to_local_coolant)
	r_door_to_local_coolant = \
		(1 / k_door_to_local_pipe) + (1 / k_local_pipe_to_local_coolant)
	r_door_to_all_local_coolant = \
		1 / (
			(1 / r_door_to_local_coolant)
			+ (1 / r_door_to_local_tile_to_local_coolant)
		)
	r_all_main_coolant_to_all_local_coolant = \
		r_all_main_coolant_to_door + r_door_to_all_local_coolant

	k_all_main_coolant_to_all_local_coolant = \
		1 / r_all_main_coolant_to_all_local_coolant

	return k_all_main_coolant_to_all_local_coolant


def lengthFromParameters (
	heat_per_second,
	main_coolant,
	main_pipe,
	main_tile,
	door,
	local_tile,
	local_pipe,
	local_coolant,
	main_coolant_exit_temperature,
	local_coolant_entry_temperature
):

	cooling = (heat_per_second > 0)

	k = kFromComponents (
		main_coolant,
		main_pipe,
		main_tile,
		door,
		local_tile,
		local_pipe,
		local_coolant,
		cooling
	)

	delta_t = local_coolant_entry_temperature - main_coolant_exit_temperature

	if (cooling and (delta_t < 0)) or ((not cooling) and delta_t > 0):
		return None

	if (main_coolant . thermal_mass == local_coolant . thermal_mass):

		return heat_per_second / (delta_t * k)

	else:

		dd = (1 / main_coolant . thermal_mass) \
			- (1 / local_coolant . thermal_mass)

		return - math . log (1 - (heat_per_second * dd)) / (k * dd)


def list (args):

	for material_name in materials . keys ():

		print (material_name)


def calculate (args):

	heat_per_second = args . heat_per_second * 1000

	main_coolant_material = materials [
		args . main_coolant_material if
			args . main_coolant_material != None else
			args . coolant_material
	]

	local_coolant_material = materials [
		args . local_coolant_material if
			args . local_coolant_material != None else
			args . coolant_material
	]

	main_coolant_mass = (
		args . main_coolant_packet_size if
			args . main_coolant_packet_size != None else
			args . coolant_packet_size
	) * 2000

	local_coolant_mass = (
		args . local_coolant_packet_size if
			args . local_coolant_packet_size != None else
			args . coolant_packet_size
	) * 2000

	main_pipe_material_name = (
		args . main_pipe_material if
			args . main_pipe_material != None else
			args . pipe_material
	)

	local_pipe_material_name = (
		args . local_pipe_material if
			args . local_pipe_material != None else
			args . pipe_material
	)

	main_tile_material_name = (
		args . main_tile_material if
			args . main_tile_material != None else
			args . tile_material
	)

	local_tile_material_name = (
		args . local_tile_material if
			args . local_tile_material != None else
			args . tile_material
	)

	door_material = materials [args . door_material]

	main_coolant_exit_temperature = args . main_coolant_exit_temperature
	local_coolant_entry_temperature = args . local_coolant_entry_temperature

	# Create objects

	main_coolant = Coolant (main_coolant_material, main_coolant_mass)
	local_coolant = Coolant (local_coolant_material, local_coolant_mass)

	main_pipe = pipeFromMaterialName (main_pipe_material_name)
	local_pipe = pipeFromMaterialName (local_pipe_material_name)

	main_tile = tileFromMaterialName (main_tile_material_name)
	local_tile = tileFromMaterialName (local_tile_material_name)

	door = Door (door_material)

	# Print result

	print (str (lengthFromParameters (
		heat_per_second,
		main_coolant,
		main_pipe,
		main_tile,
		door,
		local_tile,
		local_pipe,
		local_coolant,
		main_coolant_exit_temperature,
		local_coolant_entry_temperature
	)))


parser = ArgumentParser (
	description = "radiator.py is a simple script designed to assist in "
		"designing passive heat exchangers in Oxygen Not Included. Assumes a "
		"radiator made from two layers of tiles separated by mechanized "
		"airlocks. The coolant lines are each run through the layer of tile "
		"and the closer of the two layers of door tiles. The \"main\" coolant "
		"line is attached to a heat/cold sink. The \"local\" coolant line is "
		"the coolant loop that directly interacts with the machines or space "
		"to be heated or cooled."
)

subparsers = parser . add_subparsers (required = True, dest = 'command')

# List Command

list_parser = subparsers . add_parser (
	'list',
	help = "Lists the materials known to this utility."
)

list_parser . set_defaults (function = list)

# Calculate Command

calculate_parser = subparsers . add_parser (
	'calculate',
	help = "Calculates the required length of the heat exchanger described by "
		"the materials and parameteters."
)

calculate_parser . add_argument (
	'--heat_per_second',
	'-H',
	default = 0,
	type = float,
	required = True,
	help = "The amount of heat per second that needs to move through the heat "
		"exchanger. Negative values indicate that the heat exchanger is being "
		"used for heating rather than cooling.",
	metavar = 'kDTU'
)

## Coolant Material

calculate_parser . add_argument (
	'--coolant_material',
	'-c',
	default = 'Polluted Water',
	type = str,
	required = False,
	help = "The material used as coolant for the heat exchanger. The main "
		"line and local loop coolants are assumed to be the same.",
	metavar = "MATERIAL_NAME"
)

calculate_parser . add_argument (
	'--main_coolant_material',
	type = str,
	required = False,
	help = "The material used as coolant on the main coolant line. Overrides "
		"--coolant_material if set.",
	metavar = 'MATERIAL_NAME'
)

calculate_parser . add_argument (
	'--local_coolant_material',
	type = str,
	required = False,
	help = "The material used as coolant on the local coolant loop. Overrides "
		"--coolant_material if set.",
	metavar = 'MATERIAL_NAME'
)

## Coolant Packet Size

calculate_parser . add_argument (
	'--coolant_packet_size',
	'-s',
	default = 10,
	type = float,
	required = False,
	help = "The mass per packet of coolant. Both coolant lines are assumed to "
		"use the same packet size. 10kg is the default.",
	metavar = 'MASS_IN_KG'
)

calculate_parser . add_argument (
	'--main_coolant_packet_size',
	type = float,
	required = False,
	help = "The mass per packet of coolant on the main line. Overrides "
		"--coolant_packet_size if set.",
	metavar = 'MASS_IN_KG'
)

calculate_parser . add_argument (
	'--local_coolant_packet_size',
	type = float,
	required = False,
	help = "The mass per packet of coolant on the local loop. Overrides "
		"--coolant_packet_size if set.",
	metavar = 'MASS_IN_KG'
)

## Pipe Material

calculate_parser . add_argument (
	'--pipe_material',
	'-p',
	default = 'Copper',
	type = str,
	required = False,
	help = "The material used for the pipes in the radiator.  Both lines are "
		"assumed to use the same material. Copper is the default.",
	metavar = 'MATERIAL_NAME'
)

calculate_parser . add_argument (
	'--main_pipe_material',
	type = str,
	required = False,
	help = "The material used for the main line pipes in the radiator. "
		"Overrides --pipe_material if set.",
	metavar = 'MATERIAL_NAME'
)

calculate_parser . add_argument (
	'--local_pipe_material',
	type = str,
	required = False,
	help = "The material used for the local loop pipes in the radiator. "
		"Overrides --pipe_material if set.",
	metavar = 'MATERIAL_NAME'
)

## Tile Material

calculate_parser . add_argument (
	'--tile_material',
	'-t',
	default = 'Granite',
	type = str,
	required = False,
	help = "The material used for the tiles in the radiator. Both sides are "
		"assumed to use the same material. Granite is the default.",
	metavar = 'MATERIAL_NAME'
)

calculate_parser . add_argument (
	'--main_tile_material',
	type = str,
	required = False,
	help = "The material used for the tiles on the main line side of the "
		"radiator. Overrides --tile_material if set.",
	metavar = 'MATERIAL_NAME'
)

calculate_parser . add_argument (
	'--local_tile_material',
	type = str,
	required = False,
	help = "The material used for the tiles on the local loop side of the "
		"radiator. Overrides --tile_material if set.",
	metavar = 'MATERIAL_NAME'
)

## Door Material

calculate_parser . add_argument (
	'--door_material',
	'-d',
	default = 'Copper Ore',
	type = str,
	required = False,
	help = "The material used for the doors in the radiator. Copper Ore is the "
		"default.",
	metavar = 'MATERIAL_NAME'
)

## Main coolant exit temperature

calculate_parser . add_argument (
	'--main_coolant_exit_temperature',
	'-m',
	type = float,
	required = True,
	help = "The temperature at which the main line coolant is expected to exit "
		"the heat exchanger.",
	metavar = 'CELCIUS_OR_KELVIN'
)

## Local coolant entry temperature

calculate_parser . add_argument (
	'--local_coolant_entry_temperature',
	'-l',
	type = float,
	required = True,
	help = "The temperature at which the local loop coolant is expected to "
		"enter the heat exchanger. Note that this will be approximately the "
		"coldest or hottest temperature that you will see in the space that "
		"you are trying to heat or cool respectively.",
	metavar = 'CELCIUS_OR_KELVIN'
)

## Set commant method

calculate_parser . set_defaults (function = calculate)

# Main program

def main ():

	args = parser . parse_args ()
	args . function (args)


# Call the main program

main ()
