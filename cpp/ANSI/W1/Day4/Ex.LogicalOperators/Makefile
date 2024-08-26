CFLAGS = -std=c++03 -O2
LDFLAGS = -lglfw -lvulkan -ldl -lpthread -lX11 -lXxf86vm -lXrandr -lXi

1.1: main.cpp
	c++ $(CFLAGS) -o logicaloperators main.cpp $(LDFLAGS)

.PHONY: test clean

test: logicaloperators
	./logicaloperators

clean:
	rm -f logicaloperators
