import json_socket
import socket
import vim

class RpdbServer(object):
  def __init__(self):
    self.socket_family = socket.AF_INET
    self.socket_addr = ('localhost', 59000)

    self.conn = None
    self.jsock = None

    self.cur_file = None
    self.cur_line = None

  def connect(self):
    self.conn = socket.create_connection(self.socket_addr)
    self.jsock = json_socket.JsonSocket(self.conn)
    self.process_msg()

  def cleanup(self):
    if self.conn != None:
      self.conn.close()

  def go_to_cur_frame(self):
    if self.cur_file is None or self.cur_line is None:
      return
    go_to_loc(self.cur_file, self.cur_line)

  def set_cur_frame(self, fn, line_no):
    self.cur_file = fn
    self.cur_line = line_no
    self.go_to_cur_frame()

  def send_msg(self):
    self.jsock.send_msg()

  def do_next(self):
    self.jsock.send_msg({
      'command': 'next'})
    self.process_msg()

  def do_continue(self):
    self.jsock.send_msg({
      'command': 'continue'})
    self.process_msg()

  def do_step(self):
    self.jsock.send_msg({
      'command': 'step'})
    self.process_msg()

  def process_msg(self):
    msg = self.jsock.recv_msg()
    if msg['type'] == 'current_frame':
      self.set_cur_frame(msg['file'], msg['line_no'])

RPDB_SERVER = None

def start_debug_session():
  global RPDB_SERVER
  if RPDB_SERVER is not None:
    RPDB_SERVER.cleanup()
    RPDB_SERVER = None
  RPDB_SERVER = RpdbServer()
  RPDB_SERVER.connect()

def end_debug_session():
  global RPDB_SERVER
  if RPDB_SERVER is not None:
    RPDB_SERVER.cleanup()
    RPDB_SERVER = None

def do_next():
  RPDB_SERVER.do_next()

def do_step():
  RPDB_SERVER.do_step()

def do_continue():
  RPDB_SERVER.do_continue()

def go_to_cur_frame():
  RPDB_SERVER.go_to_cur_frame()

def go_to_loc(fn, line_no):
  vim.command('e ' + fn)
  vim.command(str(line_no))
