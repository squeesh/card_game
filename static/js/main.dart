import 'dart:html';
import 'dart:convert';

import 'controller.dart';
import 'card.dart';

List<Card> cards = [];

void main() {
  Controller ctrl = Controller.get();
  
  window.onResize.listen((e) {
    ctrl.canvas.width = window.innerWidth - 5;
    ctrl.canvas.height = window.innerHeight - 5;
  });

  var display_data = "test";
  var display_fps = "";
  
  
  ctrl.mouse_x = 0;
  ctrl.mouse_y = 0;
 
  ctrl.canvas = querySelector('#draw > canvas');
  ctrl.canvas.width = window.innerWidth - 5;
  ctrl.canvas.height = window.innerHeight - 5;
  CanvasRenderingContext2D ctx = ctrl.canvas.context2D;

  ctrl.canvas.onMouseMove.listen((MouseEvent event) {
    ctrl.mouse_x = event.client.x; 
    ctrl.mouse_y = event.client.y; 
    
    num mx = ctrl.mouse_x;
    num my = ctrl.mouse_y;
    
    display_data = "$mx | $my";
    
    for(Card card in cards) {
      card.highlight = false;
    }
    
    for(num i=cards.length-1; i >= 0; i--) {
      if(cards[i].is_over_card(ctrl.mouse_x, ctrl.mouse_y)) {
        cards[i].highlight = true;
        break;
      }
    }
  });
  
//  HttpRequest request = new HttpRequest();
//  request.open("GET", "http://192.168.1.200:8000/hand/", async: false);
//  request.setRequestHeader("Content-type", "text/plain");
//  request.overrideMimeType("text/plain; charset=x-user-defined");
  
//  request.onLoad.listen((res) {
//    window.alert(res.toString());
//  });
  
//  request.send();
  //window.alert(request.toString());
  
//  HttpRequest request = new HttpRequest();
//  request.timeout = 0;
  HttpRequest.getString("http://96.228.188.123:8000/hand/")
      .then((String fileContents) {
        print(fileContents.toString());
        
        load_cards(JSON.decode(fileContents.toString()));
      });


  DateTime old_now = new DateTime.now();
  num frames = 0;
  
  void draw(num) {
    DateTime now = new DateTime.now();
    
    ctx.save();
    
    // Use the identity matrix while clearing the canvas
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.clearRect(0, 0, ctrl.canvas.width, ctrl.canvas.height);
    
    // Restore the transform
    ctx.restore();

    ctx.fillStyle = '#000000';
    ctx.font="20px Georgia";
    ctx.textAlign = "left";
    ctx.fillText(display_data, 10, 30);
    ctx.fillText(display_fps, 10, 50);

    for(Card card in cards) {
      card.render(ctx);
    }

    if(now.millisecondsSinceEpoch - old_now.millisecondsSinceEpoch > 1000) {
      display_fps = "$frames fps";
      frames = 0;
      old_now = now;
    }
    
    frames += 1;
    
    window.animationFrame.then(draw);
  }
  
  window.animationFrame.then(draw);
}

void load_cards(data_json) {
  Controller ctrl = Controller.get();
  
  num cards_num = data_json.length;

  var i = 0;
  for(var data in data_json) {
    num x = ctrl.canvas.width * (i + 1) / (cards_num + 1.0);
    num y = ctrl.canvas.height;
    
    cards.add(new Card(x, y, data['value'], data['suit']));
    i += 1;
  }
  
//  cards_num = 11;
//    
//  for(num i=0; i < cards_num; i++) {
//    num x = ctrl.canvas.width * (i + 1) / (cards_num + 1.0);
//    num y = ctrl.canvas.height;
//    
//    cards.add(new Card(x, y, "10", "Clubs"));
//  }
}



