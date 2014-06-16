library controller;

import 'dart:html';

class Controller {
  num mouse_x;
  num mouse_y;
  
  CanvasElement canvas = null;
  
  static Controller _ctrl = null;
  
  static Controller get() {
    if(Controller._ctrl == null) {
      Controller._ctrl = new Controller();
    }
    
    return Controller._ctrl;
  }
  
}