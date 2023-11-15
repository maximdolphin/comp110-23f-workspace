"""Car driving on a road scene, with random angles of grass."""

__author__ = "730658668"

from turtle import Turtle, done
import random


def main() -> None:
    """Initialize and render the car driving on a road scene with grass."""
    car: Turtle = Turtle()
    car.speed(100)
    draw_pavement(car, -480, 0, 1000, 200)
    repeat_road_markers(car)
    draw_grass(car, -480, -500, 1000)
    draw_car(car, -100, -50)
    done()


def draw_pavement(car: Turtle, x: float, y: float, length: float, width: float) -> None:
    """Draw the road pavement."""
    car.penup()
    car.color("black", "gray")
    car.goto(x, y)
    car.pendown()
    car.begin_fill()
    i = 0
    while i < 2:
        car.forward(length)
        car.right(90)
        car.forward(width)
        car.right(90)
        i += 1
    car.end_fill()


def draw_road_markers(car: Turtle, x: float, y: float, length: float, width: float) -> None:
    """Draw individual road markers on the pavement."""
    car.penup()
    car.color("white", "white")
    car.goto(x, y)
    car.pendown()
    car.begin_fill()
    i = 0
    while i < 2:
        car.forward(length)
        car.right(90)
        car.forward(width)
        car.right(90)
        i += 1
    car.end_fill()


def repeat_road_markers(car: Turtle) -> None:
    """Draw repeated road markers on the pavement."""
    x: int = -500
    total_markers: int = 7
    used_markers: int = 0
    marker_spacing: int = 150
    while used_markers < total_markers:
        draw_road_markers(car, x, -100, 100, 20)
        x += marker_spacing
        used_markers += 1


def draw_grass(car: Turtle, x: float, y: float, length: float) -> None:
    """Draw grass strokes on the side of the pavement."""
    car.penup()
    car.color("green")
    car.goto(x, y)
    
    num_grass_strokes = int(length / 10)
    count = 0
    while count < num_grass_strokes:
        draw_single_grass_stroke(car, x + count * 10, y, 300)
        count += 1


def draw_single_grass_stroke(car: Turtle, x: float, y: float, height: float) -> None:
    """Draw a single stroke of grass."""
    car.goto(x, y)
    car.pendown()
    angle = 90 + random.randint(-15, 15)
    car.setheading(angle)
    car.forward(height)
    car.penup()


def draw_car(car: Turtle, x: float, y: float) -> None:
    """Draw a complete car including body, tires, and windows."""
    car_body(car, x, y, 200, 60)  
    car_tires(car, x + 35, y - 60, 20)  
    car_tires(car, x + 165, y - 60, 20)   
    car_windows(car, x + 30, y + 30, 140, 35) 


def car_body(car: Turtle, x: float, y: float, length: float, width: float) -> None:
    """Draw the body of the car."""
    car.penup()
    car.color("black", "red")
    car.goto(x, y)
    car.setheading(0.0)
    car.pendown()
    car.begin_fill()
    i = 0
    while i < 2:
        car.forward(length)
        car.right(90)
        car.forward(width)
        car.right(90)
        i += 1
    car.end_fill()


def car_tires(car: Turtle, x: float, y: float, radius: float) -> None:
    """Draw the tires of the car."""
    car.penup()
    car.color("black", "black")
    car.goto(x, y - radius)
    car.pendown()
    car.begin_fill()
    car.circle(radius)
    car.end_fill()


def car_windows(car: Turtle, x: float, y: float, length: float, width: float) -> None:
    """Draw the windows of the car."""
    car.penup()
    car.color("black", "blue")
    car.goto(x, y)
    car.setheading(0.0)
    car.pendown()
    car.begin_fill()
    i = 0
    while i < 2:
        car.forward(length)
        car.right(90)
        car.forward(width)
        car.right(90)
        i += 1
    car.end_fill()


if __name__ == "__main__":
    main()
