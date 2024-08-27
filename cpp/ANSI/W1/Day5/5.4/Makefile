CFLAGS = -std=c++03 -O2
LDFLAGS = -lglfw -lvulkan -ldl -lpthread -lX11 -lXxf86vm -lXrandr -lXi

1.1: main.cpp
	c++ $(CFLAGS) -o localvariables3 main.cpp $(LDFLAGS)

.PHONY: test clean

test: localvariables3
	./localvariables3

clean:
	rm -f localvariables3
