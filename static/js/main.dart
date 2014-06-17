import 'dart:html';

import 'controller.dart';


void main() {
  Controller ctrl = Controller.get();
  
  window.onResize.listen((e) {
    ctrl.canvas.width = window.innerWidth - 5;
    ctrl.canvas.height = window.innerHeight - 5;
  });

  CanvasRenderingContext2D ctx = ctrl.ctx;
  
  ctrl.add_listeners();
  ctrl.populate_hand();

  window.animationFrame.then(ctrl.render);
}



