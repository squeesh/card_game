library controller;

import 'dart:html';
import 'dart:async';
import 'dart:convert';

import 'card.dart';
import 'hand.dart';
import 'card_holder.dart';
import 'settings.dart';


class Controller {
  num mouse_x;
  num mouse_y;
  
  CanvasElement canvas = null;
  CanvasRenderingContext2D ctx = null;
  
  String display_data = "";
  String display_fps = "";
  
  PlayerHand player_1_hand;
  OpponentHand player_2_hand;
  Deck deck;
  Pile pile;
  
  num frame_count;
  
  DateTime old_now;
  
  String old_hash;
  String hash;
  
  static Controller _ctrl = null;
  
  Controller() {
    this.mouse_x = 0;
    this.mouse_y = 0;
    
    this.frame_count = 0;

    this.old_now = new DateTime.now();
    
    this.canvas = querySelector('#draw > canvas');
    this.canvas.width = window.innerWidth - 5;
    this.canvas.height = window.innerHeight - 5;
    this.ctx = this.canvas.context2D;
    
    this.player_1_hand = new PlayerHand(0, this.canvas.height);
    this.player_2_hand = new OpponentHand(0, 0);
    this.deck = new Deck(this.canvas.width / 2.0 - Card.HALF_WIDTH - 10, this.canvas.height / 2.0);
    this.pile = new Pile(this.canvas.width / 2.0 + Card.HALF_WIDTH + 10, this.canvas.height / 2.0);
    
    this.old_hash = '';
    this.hash = '';
  }
  
  void init() {
    this.add_listeners();
    this.player_1_hand.fetch();
    this.player_2_hand.fetch();
    
    new Future.delayed(VERIFY_INTERVAL, this.verify_game);
  }
  
  void verify_game() {
    this.fetch_hash();
    
    if(this.old_hash != this.hash){
      this.fetch_all();
      this.old_hash = this.hash;
    }
    
    new Future.delayed(VERIFY_INTERVAL, this.verify_game);
  }
  
  void fetch_hash() {
    HttpRequest.getString("$HOST/hash/").then((String fileContents) {
      this.hash = JSON.decode(fileContents.toString());
    });
  }
  
  void fetch_all() {
    this.player_1_hand.fetch();
    this.player_2_hand.fetch();
    this.pile.fetch();
  }
  
  void add_listeners() {
    this.canvas.onMouseMove.listen((MouseEvent event) {
      this.mouse_x = event.client.x; 
      this.mouse_y = event.client.y; 
      
      this.display_data = "$mouse_x | $mouse_y";
      
      this.player_1_hand.on_mouse_move(event);
      this.deck.on_mouse_move(event);
      this.pile.on_mouse_move(event);
    });
    
    this.canvas.onMouseDown.listen((MouseEvent event) {
      Card clicked_card = this.player_1_hand.get_highlighted_card();
      Future after_action = null;
      
      if(clicked_card != null) {
        // this.display_data = clicked_card.value + clicked_card.suit;
        after_action = this.player_1_hand.discard(clicked_card);
      } else if (this.deck.highlight == true) {
        after_action = this.deck.draw();
      } else if (this.pile.highlight == true) {
        after_action = this.pile.draw();
      }
      
      if(after_action != null) {
        after_action.then((dynamic obj) {
          this.player_1_hand.fetch();
          this.pile.fetch();
        });
      }
    });
    
    window.onResize.listen((e) {
      this.canvas.width = window.innerWidth - 5;
      this.canvas.height = window.innerHeight - 5;
      
      this.player_1_hand.y = this.canvas.height;
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

    this.player_1_hand.render(this);
    this.player_2_hand.render(this);
    this.deck.render(this);
    this.pile.render(this);

    if(now.millisecondsSinceEpoch - old_now.millisecondsSinceEpoch > 1000) {
      this.display_fps = "$frame_count fps";
      this.frame_count = 0;
      this.old_now = now;
    }
    
    this.frame_count += 1;
    
    window.animationFrame.then(this.render);
  }
}