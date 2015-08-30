"""autogenerated by genpy from robotino_motion/MotionFeedback.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import robotino_motion.msg

class MotionFeedback(genpy.Message):
  _md5sum = "49b562d6f950cdf1a89314e0d0d9f644"
  _type = "robotino_motion/MotionFeedback"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
#feedback
float32 percentage			# in range of 0% to 100%
robotino_motion/RobotState state	# d_x, d_y, d_phi, loaded
float32 elapsed_time			# in seconds
float32 expected_time			# in seconds


================================================================================
MSG: robotino_motion/RobotState
float32 d_x	#in meters/second
float32 d_y	#in meters/second
float32 d_phi	#in rad/second
bool loaded	#if true, there is a puck at robotino's grabber

"""
  __slots__ = ['percentage','state','elapsed_time','expected_time']
  _slot_types = ['float32','robotino_motion/RobotState','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       percentage,state,elapsed_time,expected_time

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(MotionFeedback, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.percentage is None:
        self.percentage = 0.
      if self.state is None:
        self.state = robotino_motion.msg.RobotState()
      if self.elapsed_time is None:
        self.elapsed_time = 0.
      if self.expected_time is None:
        self.expected_time = 0.
    else:
      self.percentage = 0.
      self.state = robotino_motion.msg.RobotState()
      self.elapsed_time = 0.
      self.expected_time = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_4fB2f.pack(_x.percentage, _x.state.d_x, _x.state.d_y, _x.state.d_phi, _x.state.loaded, _x.elapsed_time, _x.expected_time))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.state is None:
        self.state = robotino_motion.msg.RobotState()
      end = 0
      _x = self
      start = end
      end += 25
      (_x.percentage, _x.state.d_x, _x.state.d_y, _x.state.d_phi, _x.state.loaded, _x.elapsed_time, _x.expected_time,) = _struct_4fB2f.unpack(str[start:end])
      self.state.loaded = bool(self.state.loaded)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_4fB2f.pack(_x.percentage, _x.state.d_x, _x.state.d_y, _x.state.d_phi, _x.state.loaded, _x.elapsed_time, _x.expected_time))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.state is None:
        self.state = robotino_motion.msg.RobotState()
      end = 0
      _x = self
      start = end
      end += 25
      (_x.percentage, _x.state.d_x, _x.state.d_y, _x.state.d_phi, _x.state.loaded, _x.elapsed_time, _x.expected_time,) = _struct_4fB2f.unpack(str[start:end])
      self.state.loaded = bool(self.state.loaded)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_4fB2f = struct.Struct("<4fB2f")
