import cv2

class OpenFlightVideoStream:
  def __init__(self):
    self.device = None
    self.resolution = None
    self.frame_rate = None
    self.encoding_format = None
    self.writer = None

  def set_input_device(self, device):
    self.device = device

  def set_resolution(self, resolution):
    self.resolution = resolution
      
  def set_frame_rate(self, frame_rate):
    self.frame_rate = frame_rate

  def set_encoding_format(self, encoding_format):
    self.encoding_format = encoding_format

  def start(self, output_path):
    self.stream = cv2.VideoCapture(self.device)
    self.stream.set(cv2.CAP_PROP_FRAME_WIDTH, self.resolution[0])
    self.stream.set(cv2.CAP_PROP_FRAME_HEIGHT, self.resolution[1])
    self.stream.set(cv2.CAP_PROP_FPS, self.frame_rate)
    self.stream.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*self.encoding_format))
    self.writer = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*self.encoding_format), self.frame_rate, self.resolution)

  def read(self):
    ret, frame = self.stream.read()
    if ret:
      self.writer.write(frame)
    return ret, frame

  def stop(self):
    self.stream.release()
    self.writer.release()