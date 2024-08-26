CFLAGS = -std=c++03 -O2
LDFLAGS = -lglfw -lvulkan -ldl -lpthread -lX11 -lXxf86vm -lXrandr -lXi

1.1: main.cpp
	c++ $(CFLAGS) -o nestedif main.cpp $(LDFLAGS)

.PHONY: test clean

test: nestedif
	./nestedif

clean:
	rm -f nestedif
