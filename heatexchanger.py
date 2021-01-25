#!/usr/bin/python

import math
from enum import Enum
from argparse import ArgumentParser
import sys

class Material:

	def __init__ (self, heat_capacity, conductivity, properties):

		self . heat_capacity = heat_capacity
		self . conductivity = conductivity
		self . properties = properties



materials = {

# Solids

	'Algea': Material (0.2, 2, {'Organic', 'Solid'}),
	'Aluminum': Material (0.91, 205, {'Flammable', 'Generic Buildable', 'Refined Metal', 'Solid'}),
	'Aluminum Ore': Material (0.91, 20.5, {'Generic Buildable', 'Ore', 'Raw Metal', 'Solid'}),
	'Bleach Stone': Material (0.5, 4, {'Consumable Ore', 'Solid'}),
	'Ceramic': Material (0.84, 0.62, {'Crushable', 'Generic Buildable', 'Plumbable', 'Raw Mineral', 'Solid'}),
	'Clay': Material (0.92, 2, {'Cultivable Soil', 'Generic Buildable', 'Solid'}),
	'Coal': Material (0.71, 1, {'Coal', 'Consumable Ore', 'Flammable', 'Generic Buildable', 'Solid'}),
	'Copper Ore': Material (0.386, 4.5, {'Generic Buildable', 'Ore', 'Raw Metal', 'Solid'}),
	'Copper': Material (0.385, 60, {'Flammable', 'Generic Buildable', 'Refined Metal', 'Solid'}),
	'Crushed Ice': Material (2.05, 2.18, {'Ice', 'Unstable', 'Solid', 'Liquifiable'}),
	'Diamond': Material (0.516, 80, {'Generic Buildable', 'Miscellaneous', 'Solid', 'Transparent'}),
	'Dirt': Material (1.48, 2, {'Cultivable Soil', 'Generic Buildable', 'Solid'}),
	'Electrum': Material (0.15, 2, {'Generic Buildable', 'Ore', 'Raw Metal', 'Solid'}),
	'Fertilizer': Material (0.83, 2, {'Agriculture', 'Solid'}),
	'Fossil': Material (0.91, 2, {'Raw Mineral', 'Solid'}),
	'Frozen Carbon Dioxide': Material (0.846, 1.46, {'Solid'}),
	'Frozen Chlorine': Material (0.48, 0.75, {'Flammable', 'Solid', 'Toxic'}),
	'Frozen Crude Oil': Material (1.69, 2, {'Solid'}),
	'Frozen Ethanol': Material (2.46, 20, {'Flammable', 'Solid', 'Toxic'}),
	'Frozen Hydrogen': Material (2.4, 1, {'Flammable', 'Solid'}),
	'Frozen Methane': Material (2.191, 0.03, {'Consumable Ore', 'Flammable', 'Solid'}),
	'Frozen Naptha': Material (2.191, 0.2, {'Solid'}),
	'Frozen Oxygen': Material (1.01, 1, {'Solid'}),
	'Frozen Petroleum': Material (1.76, 2, {'Solid'}),
	'Frozen Super Coolant': Material (8.44, 9.46, {'Manufactured Material', 'Solid'}),
	'Frozen Visco-Gel': Material (1.55, 0.45, {'Manufactured Material', 'Plastic', 'Solid'}),
	'Fullerene': Material (0.95, 50, {'Rare Resource', 'Solid'}),
	'Glass': Material (0.84, 1.11, {'Generic Buildable', 'Manufactured Material', 'Solid', 'Transparent'}),
	'Gold': Material (0.129, 60, {'Flamable', 'Generic Buildable', 'Refined Metal', 'Solid'}),
	'Gold Amalgam': Material (0.15, 2, {'Generic Buildable', 'Ore', 'Raw Metal', 'Solid'}),
	'Granite': Material (0.79, 3.39, {'Crushable', 'Generic Buildable', 'Plumbable', 'Raw Mineral', 'Solid'}),
	'Ice': Material (2.05, 2.18, {'Ice', 'Liquifiable', 'Solid'}),
	'Igneous Rock': Material (1, 2, {'Crushable', 'Generic Buildable', 'Plumbable', 'Raw Mineral', 'Solid'}),
	'Insulation': Material (5.57, 1.0e-05, {'Crushable', 'Generic Buildable', 'Insulator', 'Manufactured Material', 'Plumbable', 'Raw Mineral', 'Solid'}),
	'Iron': Material (0.449, 55, {'Flammable', 'Generic Buildable', 'Refined Metal', 'Solid'}),
	'Iron Ore': Material (0.449, 4, {'Generic Buildable', 'Ore', 'Raw Metal', 'Solid'}),
	'Isoresin': Material (1.3, 0.17, {'Rare Resource', 'Raw Mineral', 'Solid'}),
	'Lime': Material (0.834, 2, {'Consumable Ore', 'Solid'}),
	'Mafic Rock': Material (0.2, 1, {'Generic Buildable', 'Raw Mineral', 'Solid'}),
	'Mud': Material (0.83, 2, {'Organic', 'Solid', 'Unstable'}),
	'Niobium': Material (0.265, 54, {'Generic Buildable', 'Rare Resource', 'Raw Metal', 'Refined Metal', 'Solid'}),
	'Obsidian': Material (0.2, 2, {'Crushable', 'Generic Buildable', 'Plumbable', 'Raw Mineral', 'Solid'}),
	'Oxylite': Material (1, 4, {'Consumable Ore', 'Solid'}),
	'Phosphate Nodules': Material (0.15, 2, {'Agriculture', 'Solid'}),
	'Phosphorite': Material (0.15, 2, {'Agriculture', 'Solid'}),
	'Phosphorus': Material (0.7697, 0.236, {'Consumable Ore', 'Flammable', 'Solid'}),
	'Plastic': Material (1.92, 0.15, {'Antiseptic', 'Manufactured Material', 'Plastic', 'Solid'}),
	'Polluted Dirt': Material (0.83, 2, {'Compostable', 'Organic', 'Solid', 'Unstable'}),
	'Polluted Ice': Material (3.05, 1, {'Ice', 'Liquifiable', 'Mixture', 'Solid'}),
	'Polluted Mud': Material (0.83, 2, {'Organic', 'Solid', 'Unstable'}),
	'Pyrite': Material (0.386, 4.5, {'Generic Buildable', 'Ore', 'Raw Metal', 'Solid'}),
	'Radium': Material (1, 20, {'Solid', 'Toxic'}),
	'Refined Carbon': Material (0.71, 1, {'Consumable Ore', 'Solid'}),
	'Regolith': Material (0.2, 1, {'Filtration Medium', 'Solid', 'Unstable'}),
	'Salt': Material (0.7, 0.444, {'Consumable Ore', 'Solid'}),
	'Sand': Material (0.83, 2, {'Filtration Medium', 'Solid', 'Unstable'}),
	'Sandstone': Material (0.8, 2.9, {'Crushable', 'Generic Buildable', 'Plumbable', 'Raw Mineral', 'Solid'}),
	'Sedimentary Rock': Material (0.2, 2, {'Crushable', 'Generic Buildable', 'Plumbable', 'Raw Mineral', 'Solid'}),
	'Slime': Material (0.2, 2, {'Organic', 'Solid'}),
	'Snow': Material (2.05, 0.545, {'Ice', 'Liquifiable', 'Solid', 'Unstable'}),
	'Steel': Material (0.49, 54, {'Generic Buildable', 'Manufactured Material', 'Raw Metal', 'Refined Metal', 'Solid'}),
	'Sucrose': Material (0.43, 0.444, {'Consumable Ore', 'Solid'}),
	'Sulfur': Material (0.7, 0.2, {'Solid'}),
	'Thermium': Material (0.622, 220, {'Generic Buildable', 'Manufactured Material', 'Plumbable', 'Raw Metal', 'Refined Metal', 'Solid'}),
	'Tungsten': Material (0.134, 60, {'Generic Buildable', 'Plumbable', 'Refined Metal', 'Solid'}),
	'Wolframite': Material (0.134, 15, {'Generic Buildable', 'Plumbable', 'Raw Metal', 'Solid'}),

# Liquids

	'Crude Oil': Material (1.69, 2, {'Flammable', 'Liquid', 'Toxic'}),
	'Ethanol': Material (2.46, 1.171, {'Combustable Liquid', 'Flammable', 'Liquid', 'Toxic'}),
	'Liquid Carbon Dioxide': Material (0.846, 1.46, {'Liquid'}),
	'Liquid Chlorine': Material (0.48, 0.0081, {'Flammable', 'Liquid', 'Toxic'}),
	'Liquid Hydrogen': Material (2.4, 0.1, {'Flammable', 'Liquid'}),
	'Liquid Methane': Material (2.191, 0.03, {'Flammable', 'Liquid'}),
	'Liquid Oxygen': Material (1.01, 2, {'Liquid'}),
	'Magma': Material (1, 1, {'Light Emitter', 'Liquid'}),
	'Molten Aluminum': Material (0.91, 20.5, {'Flammable', 'Light Emitter', 'Liquid', 'Raw Metal', 'Refined Metal'}),
	'Molten Carbon': Material (0.71, 2, {'Flammable', 'Liquid'}),
	'Molten Copper': Material (0.386, 12, {'Flammable', 'Light Emitter', 'Liquid', 'Raw Metal', 'Refined Metal'}),
	'Molten Glass': Material (0.2, 1, {'Light Emitter', 'Liquid'}),
	'Molten Gold': Material (0.1291, 6, {'Flammable', 'Light Emitter', 'Liquid', 'Raw Metal', 'Refined Metal'}),
	'Molten Iron': Material (0.449, 4, {'Flammable', 'Light Emitter', 'Liquid', 'Raw Metal', 'Refined Metal'}),
	'Molten Niobium': Material (0.265, 54, {'Flammable', 'Light Emitter', 'Liquid', 'Raw Metal', 'Refined Metal'}),
	'Molten Phosphorus': Material (0.7697, 0.236, {'Light Emitter', 'Liquid'}),
	'Molten Salt': Material (0.7, 0.444, {'Liquid'}),
	'Molten Steel': Material (0.386, 80, {'Flammable', 'Light Emitter', 'Liquid', 'Raw Metal', 'Refined Metal'}),
	'Molten Sulfur': Material (0.7, 0.2, {'Flammable', 'Liquid', 'Toxic'}),
	'Molten Tungsten': Material (0.134, 4, {'Liquid', 'Raw Metal', 'Refined Metal'}),
	'Naptha': Material (2.191, 0.2, {'Hydrocarbon', 'Liquid'}),
	'Petroleum': Material (1.76, 2, {'Flammable', 'Liquid', 'Toxic'}),
	'Polluted Water': Material (4.179, 0.58, {'Liquid', 'Mixture', 'Water Based'}),
	'Super Coolant': Material (8.44, 9.46, {'Liquid'}),
	'Visco-Gel': Material (1.55, 0.45, {'Liquid'}),
	'Water': Material (4.179, 0.609, {'Liquid', 'Water Based'}),

# Gasses

	'Aluminum Gas': Material (0.91, 2.5, {'Flammable', 'Gas', 'Light Emitter', 'Raw Metal', 'Refined Metal', 'Unbreathable'}),
	'Carbon Dioxide': Material (0.846, 0.0146, {'Gas', 'Unbreathable'}),
	'Carbon Gas': Material (0.71, 1.7, {'Flammable', 'Light Emitter', 'Gas', 'Unbreathable'}),
	'Chlorine': Material (0.48, 0.0081, {'Flammable', 'Gas', 'Toxic', 'Unbreathable'}),
	'Copper Gas': Material (0.386, 1, {'Flammable', 'Gas', 'Light Emitter', 'Raw Metal', 'Refined Metal', 'Unbreathable'}),
	'Ethanol Gas': Material (2.148, 0.167, {'Flammable', 'Gas', 'Toxic', 'Unbreathable'}),
	'Gold Gas': Material (0.1291, 1, {'Flammable', 'Gas', 'Light Emitter', 'Raw Metal', 'Refined Metal', 'Unbreathable'}),
	'Hydrogen': Material (2.4, 0.168, {'Flammable', 'Gas', 'Unbreathable'}),
	'Iron Gas': Material (0.449, 1, {'Flammable', 'Gas', 'Light Emitter', 'Raw Metal', 'Refined Metal', 'Unbreathable'}),
	'Natural Gas': Material (2.191, 0.035, {'Flammable', 'Gas', 'Unbreathable'}),
	'Niobium Gas': Material (0.265, 1, {'Flammable', 'Gas', 'Light Emitter', 'Raw Metal', 'Refined Metal', 'Unbreathable'}),
	'Oxygen': Material (1.005, 0.024, {'Breathable Gas', 'Gas'}),
	'Polluted Oxygen': Material (1.01, 0.024, {'Breathable Gas', 'Gas', 'Toxic'}),
	'Phosphorus Gas': Material (0.7697, 0.236, {'Flammable', 'Gas', 'Light Emitter', 'Unbreathable'}),
	'Rock Gas': Material (1, 0.1, {'Light Emitter', 'Gas', 'Unbreathable'}),
	'Salt Gas': Material (0.88, 0.444, {'Gas', 'Unbreathable Gas'}),
	'Sour Gas': Material (0.242, 0.018, {'Flammable', 'Gas', 'Unbreathable'}),
	'Steam': Material (4.179, 0.184, {'Gas', 'Unbreathable'}),
	'Steel Gas': Material (0.49, 1, {'Alloy', 'Flammable', 'Gas', 'Light Emitter', 'Raw Metal', 'Refined Metal', 'Unbreathable'}),
	'Super Coolant Gas': Material (8.44, 1.2, {'Gas', 'Unbreathable'}),
	'Sulfur Gas': Material (0.7, 0.2, {'Flammable', 'Gas', 'Unbreathable'}),
	'Tungsten Gas': Material (0.134, 1, {'Gas', 'Raw Metal', 'Refined Metal', 'Unbreathable'}),
}

def getMaterial (material_name):

	if material_name not in materials . keys ():

		raise ValueError (material_name + " is not a known material.")


	return materials [material_name]


class SolidConduit:

	def __init__ (self, material_name):

		material = getMaterial (material_name)

		if {'Solid', 'Raw Metal'} <= material . properties:

			self . conductivity = material . conductivity
			self . thermal_mass = 100000 / 5 * material . heat_capacity

		else:

			raise ValueError (material_name + " is not a valid material for building conveyor rails.")



class LiquidConduit:

	def __init__ (self, material_name):

		material = getMaterial (material_name)

		if {'Solid', 'Refined Metal'} <= material . properties:

			self . conductivity = material . conductivity * 2
			self . thermal_mass = 50000 / 5 * material . heat_capacity

		elif {'Solid', 'Plumbable'} <= material . properties:

			self . conductivity = material . conductivity
			self . thermal_mass = 100000 / 5 * material . heat_capacity

		else:

			raise ValueError (material_name + " is not a valid material for building liquid pipes.")



class GasConduit:

	def __init__ (self, material_name):

		material = getMaterial (material_name)

		if {'Solid', 'Raw Metal'} <= material . properties:

			self . conductivity = material . conductivity * 2
			self . thermal_mass = 25000 / 5 * material . heat_capacity

		elif {'Solid', 'Raw Mineral'} <= material . properties:

			self . conductivity = material . conductivity
			self . thermal_mass = 25000 / 5 * material . heat_capacity

		else:

			raise ValueError (material_name + " is not a valid material for building gas pipes.")



class Tile:

	def __init__ (self, material_name):

		material = getMaterial (material_name)

		if {'Solid', 'Raw Mineral'} <= material . properties:

			self . conductivity = material . conductivity
			self . thermal_mass = 200000 * material . heat_capacity

		elif (
			{'Solid', 'Refined Metal'} <= material . properties or
			{'Solid', 'Transparent'} <= material . properties or
			{'Solid', 'Plastic'} <= material . properties
		):

			self . conductivity = material .conductivity
			self . thermal_mass = 100000 * material . heat_capacity

		else:

			raise ValueError (material_name + " is not a valid material for building tiles.")



class MechanizedAirlock:

	def __init__ (self, material_name):

		material = getMaterial (material_name)

		if {'Solid', 'Raw Metal'} <= material . properties:

			self . conductivity = material . conductivity
			self . thermal_mass = 400000 * material . heat_capacity

		else:

			raise ValueError (material_name + " is not a valid material for building mechanized airlocks.")



class CellHalf:

	def __init__ (self, tile, coolant, n, cell_contact_ratio, flow_rate):

		self . tile = tile
		self . coolant = coolant
		self . n = n
		self . cell_contact_ratio = cell_contact_ratio
		self . flow_rate = flow_rate


	def r (self, mechanized_airlock, is_hot_side):

		m = 25 if 'Gas' in self . coolant . properties else 1

		r_at = 1 / (1000 * math . sqrt (mechanized_airlock . conductivity * self . tile . conductivity))
		r_tc = 1 / (1000 * m * self . cell_contact_ratio * math . sqrt (self . tile . conductivity * self . coolant . conductivity))
		r_tt = 1 / (1000 * self . tile . conductivity)

		return r_at + (self . n - 1) * r_tt + r_tc



class PipeHalf:

	def __init__ (self, tile, pipe, coolant, n, flow_rate):

		self . tile = tile
		self . pipe = pipe
		self . coolant = coolant
		self . n = n
		self . flow_rate = flow_rate


	def r (self, mechanized_airlock, is_hot_side):

		r_at = 1 / (25 * (self . pipe . conductivity + self . coolant . conductivity))
		r_pc = 1 / (1000 * math . sqrt (mechanized_airlock . conductivity * self . tile . conductivity))
		r_tt = 1 / (1000 * self . tile . conductivity)

		if is_hot_side:

			r_ap = 2 / (mechanized_airlock . conductivity * self . pipe . conductivity * self . pipe . thermal_mass)
			r_tp = 2 / (self . tile . conductivity * self . pipe . conductivity * self . pipe . thermal_mass)

		else:

			r_ap = 2 / (mechanized_airlock . conductivity * self . pipe . conductivity * mechanized_airlock . thermal_mass)
			r_tp = 2 / (self . tile . conductivity * self . pipe . conductivity * self . tile . thermal_mass)


		def rTiles (n):

			if n == 1:

				return 1 / (r_tp + r_pc)

			else:

				return 1 / (1 / (r_tp + r_pc) + 1 / (r_tt + rTiles (n - 1)))


		return 1 / (1 / (r_ap + r_pc) + 1 / (r_at + rTiles (self . n)))



class RailHalf:

	def __init__ (self, tile, coolant, n, flow_rate):

		self . tile = tile
		self . coolant = coolant
		self . n = n
		self . flow_rate = flow_rate


	def r (self, mechanized_airlock, is_hot_side):

		r_at = 1 / (1000 * math . sqrt (mechanized_airlock . conductivity * self . tile . conductivity))
		r_tc = 1 / (1000 * min (self . tile . conductivity, self . coolant . conductivity))
		r_ac = 1 / (1000 * min (mechanized_airlock . conductivity, self . coolant . conductivity))
		r_tt = 1 / (1000 * self . tile . conductivity)

		def rTiles (n):

			if n == 1:

				return r_tc

			else:

				return 1 / (1 / r_tc + 1 / (r_tt + rTiles (n - 1)))


		return 1 / (1 / (r_ac) + 1 / (r_at + rTiles (self . n)))



class HeatExchanger:

	def __init__ (self, mechanized_airlock, hot_side, cold_side):

		self . mechanized_airlock = mechanized_airlock
		self . hot_side = hot_side
		self . cold_side = cold_side


	def k (self):

		return 1 / (self . hot_side . r (self . mechanized_airlock, True) + self . cold_side . r (self . mechanized_airlock, False))


	def lStationaryAgainstStationary (self, dtu, delta_t_0):

		return dtu / (delta_t_0 * self . k ())


	def lFlowAgainstStationary (self, dtu, delta_t_0, thermal_flow_rate):

		return (thermal_flow_rate / self . k ()) * math . log (1 + dtu / (delta_t_0 * thermal_flow_rate))


	def lFlowAgainstFlow (self, dtu, delta_t_0, hot_thermal_flow_rate, cold_thermal_flow_rate):

		if hot_thermal_flow_rate == cold_thermal_flow_rate:

			return self . lStationaryAgainstStationary (dtu, delta_t_0)

		else:

			delta_r_thermal_flow_rate = 1 / (hot_thermal_flow_rate) - 1 / (cold_thermal_flow_rate)

			return (1 / (self . k () * delta_r_thermal_flow_rate)) * math . log (1 + (dtu * delta_r_thermal_flow_rate) / delta_t_0)


	def l (self, dtu, hot_coolant_entry_temperature, cold_coolant_entry_temperature):

		if self . hot_side . flow_rate and self . cold_side . flow_rate:

			hot_coolant_exit_temperature = hot_coolant_entry_temperature - (dtu / (self . hot_side . flow_rate * self . hot_side . coolant . heat_capacity))
			delta_t_0 = hot_coolant_exit_temperature - cold_coolant_entry_temperature

			return self . lFlowAgainstFlow (
				dtu,
				delta_t_0,
				self . hot_side . flow_rate * self . hot_side . coolant . heat_capacity,
				self . cold_side . flow_rate * self . cold_side . coolant . heat_capacity
			)

		elif self . hot_side . flow_rate:

			delta_t_0 = hot_coolant_entry_temperature - cold_coolant_entry_temperature

			return self . lFlowAgainstStationary (dtu, delta_t_0, self . hot_side . flow_rate * self . hot_side . coolant . heat_capacity)

		elif self . cold_side . flow_rate:

			delta_t_0 = hot_coolant_entry_temperature - cold_coolant_entry_temperature

			return self . lFlowAgainstStationary (dtu, delta_t_0, self . cold_side . flow_rate * self . cold_side . coolant . heat_capacity)

		else:

			delta_t_0 = hot_coolant_entry_temperature - cold_coolant_entry_temperature

			return self . lStationaryAgainstStationary (dtu, delta_t_0)



def list (args):

	for material_name in materials . keys ():

		print (material_name)


exchanger_config_choices = ['stationary', 'waterfall', 'conduits']

def calculate (args):

	mechanized_airlock = MechanizedAirlock (args . mechanized_airlock_material)

	dtu = args . heat_per_second * 1000

	hot_interface = args . hot_interface if args . hot_interface else args . interface
	cold_interface = args . cold_interface if args . cold_interface else args . interface

	if hot_interface == 'stationary':

		coolant = getMaterial (args . cold_coolant if args . cold_coolant else args . coolant)
		contact_ratio = args . hot_coolant_contact_ratio if args . hot_coolant_contact_ratio else args . coolant_contact_ratio
		tile = Tile (args . hot_tile_material if args . hot_tile_material else args . tile_material)
		num_tiles = args . num_hot_tiles if args . num_hot_tiles else args . num_tiles

		if args . hot_conduit_material:
			raise ValueError ("Stationary interfaces do not contain conduits.")

		if args . hot_coolant_flow_rate:
			raise ValueError ("Stationary interfaces do not have flowing coolant.")

		if args . hot_coolant_entry_temperature or args . hot_coolant_exit_temperature:
			raise ValueError ("Stationary interfaces don't have coolant exit/entry temperatures.  Use the --X-coolant-temperature option for stationary interfaces.")

		hot_side = CellHalf (tile, coolant, num_tiles, contact_ratio, 0)
		hot_coolant_entry_temperature = args . hot_coolant_temperature

	elif hot_interface == 'waterfall':

		coolant = getMaterial (args . cold_coolant if args . cold_coolant else args . coolant)
		flow_rate = (args . hot_coolant_flow_rate if args . hot_coolant_flow_rate else args . coolant_flow_rate) * 1000
		contact_ratio = args . hot_coolant_contact_ratio if args . hot_coolant_contact_ratio else args . coolant_contact_ratio
		tile = Tile (args . hot_tile_material if args . hot_tile_material else args . tile_material)
		num_tiles = args . num_hot_tiles if args . num_hot_tiles else args . num_tiles

		if args . hot_conduit_material:
			raise ValueError ("Waterfall interfaces do not contain conduits.")

		if args . hot_coolant_temperature:
			raise ValueError ("You must specify an entry or exit temperature for flowing coolants.")

		if 'Solid' in coolant . properties:
			raise ValueError ("Waterfalls cannot be made out of solids.")

		hot_side = CellHalf (tile, coolant, num_tiles, contact_ratio, flow_rate)
		hot_coolant_entry_temperature = (
			args . hot_coolant_entry_temperature if args . hot_coolant_entry_temperature
			else args . hot_coolant_exit_temperature + (dtu / (flow_rate * coolant . heat_capacity))
		)

	elif hot_interface == 'conduits':

		coolant = getMaterial (args . hot_coolant if args . hot_coolant else args . coolant)
		flow_rate = (args . hot_coolant_flow_rate if args . hot_coolant_flow_rate else args . coolant_flow_rate) * 1000
		tile = Tile (args . hot_tile_material if args . hot_tile_material else args . tile_material)
		num_tiles = args . num_hot_tiles if args . num_hot_tiles else args . num_tiles

		conduit_material = args . hot_conduit_material if args . hot_conduit_material else args . conduit_material

		if args . hot_coolant_contact_ratio:
			raise ValueError ("Don't space out packets of coolant. Use a valve to control the flow rate instead.")

		if args . hot_coolant_temperature:
			raise ValueError ("You must specify an entry or exit temperature for flowing coolants.")

		if 'Solid' in coolant . properties:

			if args . hot_conduit_material:
				raise ValueError ("The material used to construct the conveyor rails is irrelevant.")

			hot_side = RailHalf (tile, coolant, num_tiles, flow_rate)

		elif 'Liquid' in coolant . properties:

			conduit = LiquidConduit (conduit_material)

			hot_side = PipeHalf (tile, conduit, coolant, num_tiles, flow_rate)

		elif 'Gas' in coolant . properties:

			conduit = GasConduit (conduit_material)

			hot_side = PipeHalf (tile, conduit, coolant, num_tiles, flow_rate)

		hot_coolant_entry_temperature = (
			args . hot_coolant_entry_temperature if args . hot_coolant_entry_temperature
			else args . hot_coolant_exit_temperature + (dtu / (flow_rate * coolant . heat_capacity))
		)


	if cold_interface == 'stationary':

		coolant = getMaterial (args . cold_coolant if args . cold_coolant else args . coolant)
		contact_ratio = args . cold_coolant_contact_ratio if args . cold_coolant_contact_ratio else args . coolant_contact_ratio
		tile = Tile (args . cold_tile_material if args . cold_tile_material else args . tile_material)
		num_tiles = args . num_cold_tiles if args . num_cold_tiles else args . num_tiles

		if args . cold_conduit_material:
			raise ValueError ("Stationary interfaces do not contain conduits.")

		if args . cold_coolant_flow_rate:
			raise ValueError ("Stationary interfaces do not have flowing coolant.")

		if args . cold_coolant_entry_temperature or args . cold_coolant_exit_temperature:
			raise ValueError ("Stationary interfaces don't have coolant exit/entry temperatures. Use the --X-coolant-temperature option for stationary interfaces.")

		cold_side = CellHalf (tile, coolant, num_tiles, contact_ratio, 0)
		cold_coolant_entry_temperature = args . cold_coolant_temperature

	elif cold_interface == 'waterfall':

		coolant = getMaterial (args . cold_coolant if args . cold_coolant else args . coolant)
		flow_rate = (args . cold_coolant_flow_rate if args . cold_coolant_flow_rate else args . coolant_flow_rate) * 1000
		contact_ratio = args . cold_coolant_contact_ratio if args . cold_coolant_contact_ratio else args . coolant_contact_ratio
		tile = Tile (args . cold_tile_material if args . cold_tile_material else args . tile_material)
		num_tiles = args . num_cold_tiles if args . num_cold_tiles else args . num_tiles

		if args . cold_conduit_material:
			raise ValueError ("Waterfall interfaces do not contain conduits.")

		if args . cold_coolant_temperature:
			raise ValueError ("You must specify an entry or exit temperature for flowing coolants.")

		if 'Solid' in coolant . properties:
			raise ValueError ("Waterfalls cannot be made out of solids.")

		cold_side = CellHalf (tile, coolant, num_tiles, contact_ratio, flow_rate)
		cold_coolant_entry_temperature = (
			args . cold_coolant_entry_temperature if args . cold_coolant_entry_temperature
			else args . cold_coolant_exit_temperature - (dtu / (flow_rate * coolant . heat_capacity))
		)

	elif cold_interface == 'conduits':

		coolant = getMaterial (args . cold_coolant if args . cold_coolant else args . coolant)
		flow_rate = (args . cold_coolant_flow_rate if args . cold_coolant_flow_rate else args . coolant_flow_rate) * 1000
		tile = Tile (args . cold_tile_material if args . cold_tile_material else args . tile_material)
		num_tiles = args . num_cold_tiles if args . num_cold_tiles else args . num_tiles

		conduit_material = args . cold_conduit_material if args . cold_conduit_material else args . conduit_material

		if args . cold_coolant_contact_ratio:
			raise ValueError ("Don't space out packets of coolant. Use a valve to control the flow rate instead.")

		if args . cold_coolant_temperature:
			raise ValueError ("You must specify an entry or exit temperature for flowing coolants.")

		if 'Solid' in coolant . properties:

			if args . cold_conduit_material:
				raise ValueError ("The material used to construct the conveyor rails is irrelevant.")

			cold_side = RailHalf (tile, coolant, num_tiles, flow_rate)

		elif 'Liquid' in coolant . properties:

			conduit = LiquidConduit (conduit_material)

			cold_side = PipeHalf (tile, conduit, coolant, num_tiles, flow_rate)

		elif 'Gas' in coolant . properties:

			conduit = GasConduit (conduit_material)

			cold_side = PipeHalf (tile, conduit, coolant, num_tiles, flow_rate)

		cold_coolant_entry_temperature = (
			args . cold_coolant_entry_temperature if args . cold_coolant_entry_temperature
			else args . cold_coolant_exit_temperature - (dtu / (flow_rate * coolant . heat_capacity))
		)


	heat_exchanger = HeatExchanger (mechanized_airlock, hot_side, cold_side)

	print (heat_exchanger . l (dtu, hot_coolant_entry_temperature, cold_coolant_entry_temperature))


parser = ArgumentParser (
	description = sys . argv [0] + " is a simple script designed to assist in "
		"designing passive heat exchangers in Oxygen Not Included. Assumes a "
		"heat exchanger made from layers of tiles separated by mechanized "
		"airlocks."
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

## Mechanized Airlock Material

calculate_parser . add_argument (
	'--mechanized-airlock-material',
	'-a',
	default = 'Copper Ore',
	type = str,
	required = False,
	help = "The material used for the mechanized_airlocks in the radiator. "
		"Copper Ore is the default.",
	metavar = 'MATERIAL_NAME'
)

## Exchanger Configuration

calculate_parser . add_argument (
	'--interface',
	'-i',
	default = 'conduits',
	choices = exchanger_config_choices,
	required = False,
	help = "The interface that the heat exchanger uses to exchange heat with "
		"the coolant. The hot and cold sides are assumed to use the same "
		"interface.",
	metavar = "INTERFACE"
)

calculate_parser . add_argument (
	'--hot-interface',
	choices = exchanger_config_choices,
	required = False,
	help = "The interface that the heat exchanger uses to exchange heat with "
		"the hot coolant.  Overrides --interface if set.",
	metavar = "INTERFACE"
)

calculate_parser . add_argument (
	'--cold-interface',
	choices = exchanger_config_choices,
	required = False,
	help = "The interface that the heat exchanger uses to exchange heat with "
		"the cold coolant.  Overrides --interface if set.",
	metavar = "INTERFACE"
)

## Coolant Material

calculate_parser . add_argument (
	'--coolant',
	'-c',
	default = 'Polluted Water',
	type = str,
	required = False,
	help = "The material used as coolant for the heat exchanger. The hot and "
		"cold coolants are assumed to be the same.",
	metavar = "MATERIAL_NAME"
)

calculate_parser . add_argument (
	'--hot-coolant',
	type = str,
	required = False,
	help = "The material used as coolant on the hot side. Overrides "
		"--coolant-material if set.",
	metavar = 'MATERIAL_NAME'
)

calculate_parser . add_argument (
	'--cold-coolant',
	type = str,
	required = False,
	help = "The material used as coolant on the cold side. Overrides "
		"--coolant-material if set.",
	metavar = 'MATERIAL_NAME'
)

## Coolant Flow Rate

calculate_parser . add_argument (
	'--coolant-flow-rate',
	'-f',
	default = 10,
	type = float,
	required = False,
	help = "The mass per packet of coolant. Both coolant sides are assumed to "
		"use the same flow rate.",
	metavar = 'KG_PER_SECOND'
)

calculate_parser . add_argument (
	'--hot-coolant-flow-rate',
	type = float,
	required = False,
	help = "The flow rate of the coolant on the hot side. Overrides "
		"--coolant-flow-rate if set.",
	metavar = 'KG_PER_SECOND'
)

calculate_parser . add_argument (
	'--cold-coolant-flow-rate',
	type = float,
	required = False,
	help = "The flow rate of the foolant on the cold side. Overrides "
		"--coolant-flow-rate if set.",
	metavar = 'KG_PER_SECOND'
)

## Coolant Contact Ratio

calculate_parser . add_argument (
	'--coolant-contact-ratio',
	default = 1,
	type = float,
	required = False,
	help = "The ratio of coolant cells to empty cells in the waterfall "
		"interfaces. The hot and cold sides are assumed to have the same "
		"contact ratio.",
	metavar = 'CONTACT_RATIO'
)

calculate_parser . add_argument (
	'--hot-coolant-contact-ratio',
	type = float,
	required = False,
	help = "The ratio of coolant cells to empty cells in the hot waterfall "
		"interface. Overrides --coolant-contact-ratio if set.",
	metavar = 'CONTACT_RATIO'
)

calculate_parser . add_argument (
	'--cold-coolant-contact-ratio',
	type = float,
	required = False,
	help = "The ratio of coolant cells to empty cells in the cold waterfall "
		"interface. Overrides --coolant-contact-ratio if set.",
	metavar = 'CONTACT_RATIO'
)

## Tile Material

calculate_parser . add_argument (
	'--tile-material',
	'-t',
	default = 'Granite',
	type = str,
	required = False,
	help = "The material used for the tiles in the heat exchanger. Both sides "
		"are assumed to use the same material. Granite is the default.",
	metavar = 'MATERIAL_NAME'
)

calculate_parser . add_argument (
	'--hot-tile-material',
	type = str,
	required = False,
	help = "The material used for the tiles on the hot side of the heat"
		"exchanger. Overrides --tile-material if set.",
	metavar = 'MATERIAL_NAME'
)

calculate_parser . add_argument (
	'--cold-tile-material',
	type = str,
	required = False,
	help = "The material used for the tiles on the cold side of the heat"
		"exchanger. Overrides --tile-material if set.",
	metavar = 'MATERIAL_NAME'
)

# Number of Tiles

calculate_parser . add_argument (
	'--num-tiles',
	'-n',
	default = 1,
	type = int,
	required = False,
	help = "The number of tiles past the mechanized airlocks. Both sides are "
		"assumed to use the same number of tiles. The default value is 1.",
	metavar = 'N'
)

calculate_parser . add_argument (
	'--num-hot-tiles',
	type = int,
	required = False,
	help = "The number of tiles past the mechanized airlocks on the hot side. "
		"Overrides --num-tiles if set.",
	metavar = 'N'
)

calculate_parser . add_argument (
	'--num-cold-tiles',
	type = int,
	required = False,
	help = "The number of tiles past the mechanized airlocks on the cold side. "
		"Overrides --num-tiles if set.",
	metavar = 'N'
)

## Conduit Material

calculate_parser . add_argument (
	'--conduit-material',
	'-p',
	default = 'Copper',
	type = str,
	required = False,
	help = "The material used for the conduits (pipes/conveyor rails) in the "
		"heat exchanger.  Both sides are assumed to use the same material. "
		"Copper is the default.",
	metavar = 'MATERIAL_NAME'
)

calculate_parser . add_argument (
	'--hot-conduit-material',
	type = str,
	required = False,
	help = "The material used on the hot side of the heat exchanger. "
		"Overrides --conduit-material if set.",
	metavar = 'MATERIAL_NAME'
)

calculate_parser . add_argument (
	'--cold-conduit-material',
	type = str,
	required = False,
	help = "The material used on the cold side of the heat exchanger. "
		"Overrides --conduit-material if set.",
	metavar = 'MATERIAL_NAME'
)

## DTU per Second

calculate_parser . add_argument (
	'--heat-per-second',
	'-H',
	default = 0,
	type = float,
	required = True,
	help = "The amount of heat per second that needs to move through the heat "
		"exchanger.",
	metavar = 'kDTU'
)

## Hot Coolant Temperature

hot_coolant_temp_group = \
	calculate_parser . add_mutually_exclusive_group (required = True)

hot_coolant_temp_group . add_argument (
	'--hot-coolant-temperature',
	type = float,
	required = False,
	help = "The temperature of the stationary hot coolant.",
	metavar = 'CELCIUS_OR_KELVIN'
)

hot_coolant_temp_group . add_argument (
	'--hot-coolant-entry-temperature',
	type = float,
	required = False,
	help = "The temperature at which the hot coolant is expected to enter the "
		"heat exchanger.",
	metavar = 'CELCIUS_OR_KELVIN'
)

hot_coolant_temp_group . add_argument (
	'--hot-coolant-exit-temperature',
	type = float,
	required = False,
	help = "The temperature at which the hot coolant is expected to exit the "
		"heat exchanger.",
	metavar = 'CELCIUS_OR_KELVIN'
)

## Cold Coolant Temperature

cold_coolant_temp_group = \
	calculate_parser . add_mutually_exclusive_group (required = True)

cold_coolant_temp_group . add_argument (
	'--cold-coolant-temperature',
	type = float,
	required = False,
	help = "The temperature of the stationary cold coolant.",
	metavar = 'CELCIUS_OR_KELVIN'
)

cold_coolant_temp_group . add_argument (
	'--cold-coolant-entry-temperature',
	type = float,
	required = False,
	help = "The temperature at which the cold coolant is expected to enter the "
		"heat exchanger.",
	metavar = 'CELCIUS_OR_KELVIN'
)

cold_coolant_temp_group . add_argument (
	'--cold-coolant-exit-temperature',
	type = float,
	required = False,
	help = "The temperature at which the cold coolant is expected to exit the "
		"heat exchanger.",
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
