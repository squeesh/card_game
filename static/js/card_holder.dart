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
  
  Future<Card> _get_card_from_url(String url) {
    return HttpRequest.getString(url).then((String fileContents) {
      var json_data = JSON.decode(fileContents.toString());
      if(json_data != null) {
        return new Card(json_data['value'], json_data['suit']);
      } else {
        return null;
      }      
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
    return this._get_card_from_url("$HOST/draw-deck/");
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
  Card top_card = null;
  
  Pile(num x, num y) : super(x, y) {
    this.fetch();
  }
  
  Future<Card> draw() {
    return this._get_card_from_url("$HOST/draw-pile/");
  }
  
  Future<Card> fetch() {
    return this._get_card_from_url("$HOST/pile/").then((Card card) => this.top_card = card);
  }
  
  void render(Controller ctrl) {
    super.render(ctrl);
    
    if(this.top_card != null) {
      this.top_card.render(ctrl, this.x, this.y);
    }
  }
  
  void on_mouse_move(MouseEvent event) {
    super.on_mouse_move(event);
    if(this.top_card != null) {
      this.top_card.highlight = this.highlight;
    }
  }
}