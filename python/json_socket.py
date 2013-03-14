import socket
import json

class JsonSocket(object):
  def __init__(self, sock):
    self.sock = sock
    self.data = ''

  def recv_msg(self):
    eos = self.data.find('\r\n')
    while eos < 0:
      chunk = self.sock.recv(1024)
      if len(chunk) == 0:
        return None
      self.data += chunk
      eos = self.data.find('\r\n')
    size = int(self.data[:eos])

    self.data = self.data[eos+2:]
    while len(self.data) < size:
      chunk = self.sock.recv(1024)
      if len(chunk) == 0:
        return None
      self.data += chunk

    json_str = self.data[:size]
    self.data = self.data[size:]
    return json.loads(json_str)

  def send_msg(self, obj):
    obj_json = json.dumps(obj)
    msg_sz = len(obj_json)
    self.sock.sendall(str(msg_sz) + '\r\n' + obj_json)

  def close(self):
    self.sock.close()
