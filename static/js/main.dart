import 'dart:html';

import 'controller.dart';


void main() {
  Controller ctrl = Controller.get();

  CanvasRenderingContext2D ctx = ctrl.ctx;
  
  ctrl.add_listeners();
  ctrl.fetch_hand();

  window.animationFrame.then(ctrl.render);
}
