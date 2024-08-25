CFLAGS = -std=c++03 -O2
LDFLAGS = -lglfw -lvulkan -ldl -lpthread -lX11 -lXxf86vm -lXrandr -lXi

1.1: main.cpp
	c++ $(CFLAGS) -o printchars2 main.cpp $(LDFLAGS)

.PHONY: test clean

test: printchars2
	./printchars2

clean:
	rm -f printchars2
