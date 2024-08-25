CFLAGS = -std=c++03 -O2
LDFLAGS = -lglfw -lvulkan -ldl -lpthread -lX11 -lXxf86vm -lXrandr -lXi

1.1: main.cpp
	c++ $(CFLAGS) -o enumeratedconstants2 main.cpp $(LDFLAGS)

.PHONY: test clean

test: enumeratedconstants2
	./enumeratedconstants2

clean:
	rm -f enumeratedconstants2
