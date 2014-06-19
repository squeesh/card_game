import 'dart:html';

import 'controller.dart';


void main() {
  Controller ctrl = Controller.get();

  CanvasRenderingContext2D ctx = ctrl.ctx;
  
  ctrl.init();
  
  window.animationFrame.then(ctrl.render);
}
