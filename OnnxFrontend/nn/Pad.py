import numpy as np

class Pad_1:

	mode = m_str()
	paddings = m_list()
	value = m_float()
	def __init__(self, _name: str, mode: str, paddings: list, value: float):
		self.name = _name
		self.m_mode = mode
		self.m_paddings = paddings
		self.m_value = value

	def __call__(self, data: str):
		 return output


class Pad_2:

	mode = m_str()
	pads = m_list()
	value = m_float()
	def __init__(self, _name: str, mode: str, pads: list, value: float):
		self.name = _name
		self.m_mode = mode
		self.m_pads = pads
		self.m_value = value

	def __call__(self, data: str):
		 return output