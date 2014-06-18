library card_holder;

import 'dart:html';
import 'dart:async';
import 'dart:convert';

import 'controller.dart';
import 'card.dart';
import 'settings.dart';


abstract class CardHolder {
  num x;
  num y;
  
  bool highlight = false;
  
  static num HALF_WIDTH  = Card.HALF_WIDTH  + 5;
  static num HALF_HEIGHT = Card.HALF_HEIGHT + 5;
  
  CardHolder(this.x, this.y);
  
  Future<Card> draw();
  
  Future<Card> _draw(String url) {
    return HttpRequest.getString(url).then((String fileContents) {
      var json_data = JSON.decode(fileContents.toString());
      return new Card(json_data['value'], json_data['suit']);
    });
  }
  
  void render(Controller ctrl) {
    CanvasRenderingContext2D ctx = ctrl.ctx;
    
    if(this.highlight == true) {
      ctx.strokeStyle = '#00BB00';
    } else {
      ctx.strokeStyle = '#000000';
    }

    ctx.strokeRect(
        this.x - CardHolder.HALF_WIDTH, this.y - CardHolder.HALF_HEIGHT,
        CardHolder.HALF_WIDTH * 2, CardHolder.HALF_HEIGHT * 2
    );
  }
  
  void on_mouse_move(MouseEvent event) {
    num mouse_x = event.client.x;
    num mouse_y = event.client.y;

    if( mouse_x > (this.x - CardHolder.HALF_WIDTH)  && 
        mouse_x < (this.x + CardHolder.HALF_WIDTH)  &&
        mouse_y > (this.y - CardHolder.HALF_HEIGHT) && 
        mouse_y < (this.y + CardHolder.HALF_HEIGHT)) {
      this.highlight = true;
    } else {
      this.highlight = false;
    }
  }
}

class Deck extends CardHolder {
  Deck(num x, num y) : super(x, y);
  
  Future<Card> draw() {
    return this._draw(HOST + "/draw-deck/");
  }
  
  void render(Controller ctrl) {
    super.render(ctrl);
    
    CanvasRenderingContext2D ctx = ctrl.ctx;
  
    if(this.highlight == true) {
      ctx.fillStyle = '#999900';
    } else {
      ctx.fillStyle = '#660000';
    }

    ctx.fillRect(
        this.x - Card.HALF_WIDTH, this.y - Card.HALF_HEIGHT,
        Card.HALF_WIDTH * 2, Card.HALF_HEIGHT * 2
    );
  }
}

class Pile extends CardHolder {
  Pile(num x, num y) : super(x, y);
  
  Future<Card> draw() {
    return this._draw(HOST + "/draw-pile/");
  }
}