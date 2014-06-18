library hand;

import 'dart:html';
import 'dart:async';
import 'dart:convert';

import 'controller.dart';
import 'card.dart';
import 'settings.dart';

class Hand {
  num x;
  num y;
  List<Card> cards = null;
  
  Hand(num x, num y) {
    this.x = x;
    this.y = y;
    this.cards = [];
  }
  
  void fetch() {
    HttpRequest.getString("$HOST/hand/").then((String fileContents) {
      Controller ctrl = Controller.get();
      
      var json_data = JSON.decode(fileContents.toString());
      num cards_num = json_data.length;

      this.cards = [];
      
      for(var data in json_data) {
        this.cards.add(new Card(data['value'], data['suit']));
      }
    });
  }
  
  Future discard(Card card) {
    num card_pos = this.cards.indexOf(card);
    return HttpRequest.getString("$HOST/discard/$card_pos/");
  }
  
  void render(Controller ctrl) {
    num cards_num = this.cards.length;
    
    for(num i=0; i < cards_num; i++) {
      Card curr_card = this.cards[i];
      
      num card_x = this.x + ctrl.canvas.width * (i + 1) / (cards_num + 1.0);

      curr_card.render(ctrl, card_x, this.y);
    }
  }
  
  Card _get_hovered_card(num mouse_x, num mouse_y) {
    Controller ctrl = Controller.get();

    num card_y = this.y;
    num cards_num = this.cards.length;

    for(num i=cards_num-1; i >= 0; i--) {
      Card curr_card = this.cards[i];
      num card_x = this.x + ctrl.canvas.width * (i + 1) / (cards_num + 1.0);
      
      if( mouse_x > (card_x - Card.HALF_WIDTH)  && 
          mouse_x < (card_x + Card.HALF_WIDTH)  &&
          mouse_y > (card_y - Card.HALF_HEIGHT) && 
          mouse_y < (card_y + Card.HALF_HEIGHT)) {
        return curr_card;
      }
    }
    
    return null;
  }
  
  Card get_highlighted_card() {
    for(Card card in this.cards){
      if(card.highlight == true) {
        return card;
      }
    }
    
    return null;
  }
  
  void on_mouse_move(MouseEvent event) {
    num mx = event.client.x;
    num my = event.client.y;

    for(Card card in this.cards) {
      card.highlight = false;
    }

    Card hovered_card = this._get_hovered_card(mx, my);
    
    if(hovered_card != null) {
      hovered_card.highlight = true;
    }
  }
}