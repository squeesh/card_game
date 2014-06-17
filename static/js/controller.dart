library controller;

import 'dart:html';
import 'dart:convert';

import 'card.dart';


class Controller {
  num mouse_x;
  num mouse_y;
  
  CanvasElement canvas = null;
  CanvasRenderingContext2D ctx = null;
  
  String display_data = "";
  String display_fps = "";
  
  List<Card> cards = null;
  
  num frame_count;
  
  DateTime old_now;
  
  static Controller _ctrl = null;
  
  Controller() {
    this.mouse_x = 0;
    this.mouse_y = 0;
    
    this.frame_count = 0;
    
    this.cards = [];
    
    this.old_now = new DateTime.now();
    
    this.canvas = querySelector('#draw > canvas');
    this.canvas.width = window.innerWidth - 5;
    this.canvas.height = window.innerHeight - 5;
    this.ctx = this.canvas.context2D;

  }
  
  void add_listeners() {
    this.canvas.onMouseMove.listen((MouseEvent event) {
      this.mouse_x = event.client.x; 
      this.mouse_y = event.client.y; 
      
      num mx = this.mouse_x;
      num my = this.mouse_y;
      
      this.display_data = "$mx | $my";
      
      for(Card card in this.cards) {
        card.highlight = false;
      }
      
      for(num i=this.cards.length-1; i >= 0; i--) {
        if(this.cards[i].is_over_card(this.mouse_x, this.mouse_y)) {
          this.cards[i].highlight = true;
          break;
        }
      }
    });
  }
  
  void populate_hand() {
    HttpRequest.getString("http://squeesh.net:8000/hand/").then((String fileContents) {
      Controller ctrl = Controller.get();
      
      var json_data = JSON.decode(fileContents.toString());
      num cards_num = json_data.length;

      num i = 0;
      for(var data in json_data) {
        num x = ctrl.canvas.width * (i + 1) / (cards_num + 1.0);
        num y = ctrl.canvas.height;
        
        ctrl.cards.add(new Card(x, y, data['value'], data['suit']));
        i += 1;
      }
    });
  }
  
  static Controller get() {
    if(Controller._ctrl == null) {
      Controller._ctrl = new Controller();
    }
    
    return Controller._ctrl;
  }
  
  void render(num time) {
    DateTime now = new DateTime.now();
    
    this.ctx.save();
    
    // Use the identity matrix while clearing the canvas
    this.ctx.setTransform(1, 0, 0, 1, 0, 0);
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    
    // Restore the transform
    this.ctx.restore();

    this.ctx.fillStyle = '#000000';
    this.ctx.font="20px Georgia";
    this.ctx.textAlign = "left";
    this.ctx.fillText(this.display_data, 10, 30);
    this.ctx.fillText(this.display_fps, 10, 50);

    for(Card card in this.cards) {
      card.render(this.ctx);
    }

    if(now.millisecondsSinceEpoch - old_now.millisecondsSinceEpoch > 1000) {
      this.display_fps = "$frame_count fps";
      this.frame_count = 0;
      this.old_now = now;
    }
    
    this.frame_count += 1;
    
    window.animationFrame.then(this.render);
  }
}