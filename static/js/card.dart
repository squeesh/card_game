library card;

import 'dart:html';

import 'controller.dart';

class Card {
  num x;
  num y;
  bool highlight = false;
  
  num HALF_WIDTH = 100;
  num HALF_HEIGHT = 150;
  
  String value = "5";
  String suit = "Hearts";
  
  Card(this.x, this.y, this.value, this.suit);
  
  void render(CanvasRenderingContext2D ctx) {
    Controller ctrl = Controller.get();
    
    num offset = 0;
    
    if(this.highlight) {
      ctx.fillStyle = '#00ff00';
      offset = 30;
    } else {
      ctx.fillStyle = '#ff0000';
    }
    
    ctx.fillRect(
        this.x - this.HALF_WIDTH, this.y - this.HALF_HEIGHT - offset,
        this.HALF_WIDTH * 2, this.HALF_HEIGHT * 2
    );
    
    ctx.strokeStyle = '#000000';
    ctx.strokeRect(
        this.x - this.HALF_WIDTH, this.y - this.HALF_HEIGHT - offset,
        this.HALF_WIDTH * 2, this.HALF_HEIGHT * 2
    );
    
    ctx.fillStyle = '#000000';
    ctx.font="20px Georgia";
    ctx.textAlign = "center";
    ctx.fillText(this.value + this.suit, this.x, this.y - (this.HALF_HEIGHT / 2.0) - offset);
//    ctx.fillText(this.suit,  this.x, this.y - (this.HALF_HEIGHT / 2.0) + 20);
  }
  
  bool is_over_card(num mouse_x, num mouse_y) {
    return (
        mouse_x > (this.x - this.HALF_WIDTH) && 
        mouse_x < (this.x + this.HALF_WIDTH) &&
        mouse_y > (this.y - this.HALF_HEIGHT) && 
        mouse_y < (this.y + this.HALF_HEIGHT)
    );
  }
}