library card;

import 'dart:html';

import 'controller.dart';

class Card {
  bool highlight = false;

  static num HALF_WIDTH = 100;
  static num HALF_HEIGHT = 150;
  
  String value = "5";
  String suit = "Hearts";
  
  Card(this.value, this.suit);
  
  void render(Controller ctrl, num x, num y) {
    CanvasRenderingContext2D ctx = ctrl.ctx;

    if(this.highlight) {
      ctx.fillStyle = '#ccccdd';
    } else {
      ctx.fillStyle = '#cccccc';
    }
    
    ctx.fillRect(
        x - Card.HALF_WIDTH, y - Card.HALF_HEIGHT,
        Card.HALF_WIDTH * 2, Card.HALF_HEIGHT * 2
    );
    
    ctx.strokeStyle = '#000000';
    ctx.strokeRect(
        x - Card.HALF_WIDTH, y - Card.HALF_HEIGHT,
        Card.HALF_WIDTH * 2, Card.HALF_HEIGHT * 2
    );
    
    List<String> red_suits = ['♥', '♦'];
    
    if(red_suits.contains(this.suit)) {
      ctx.fillStyle = '#AA0000';
    } else {
      ctx.fillStyle = '#000000';
    }
    
    // Top left of card
    ctx.font="20px Georgia";
    ctx.textAlign = "left";
    ctx.fillText(this.value + this.suit, x - Card.HALF_WIDTH + 5, y - Card.HALF_HEIGHT + 20);
    
    // Bottom Right of card
    ctx.textAlign = "right";
    ctx.fillText(this.value + this.suit, x + Card.HALF_WIDTH - 5, y + Card.HALF_HEIGHT - 10);
    
    // Center of card
    ctx.font="50px Georgia";
    ctx.textAlign = "center";
    ctx.fillText(this.suit, x, y + 20);
  }
  
}