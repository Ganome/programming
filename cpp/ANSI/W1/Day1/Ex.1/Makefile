CFLAGS = -std=c++11 -O2
LDFLAGS = -lglfw -lvulkan -ldl -lpthread -lX11 -lXxf86vm -lXrandr -lXi

1.1: main.cpp
	c++ $(CFLAGS) -o math main.cpp $(LDFLAGS)

.PHONY: test clean

test: math
	./math

clean:
	rm -f math
