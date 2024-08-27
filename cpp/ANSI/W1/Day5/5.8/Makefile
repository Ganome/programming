CFLAGS = -std=c++03 -O2
LDFLAGS = -lglfw -lvulkan -ldl -lpthread -lX11 -lXxf86vm -lXrandr -lXi

1.1: main.cpp
	c++ $(CFLAGS) -o polymorphism main.cpp $(LDFLAGS)

.PHONY: test clean

test: polymorphism
	./polymorphism

clean:
	rm -f polymorphism
