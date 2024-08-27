CFLAGS = -std=c++03 -O2
LDFLAGS = -lglfw -lvulkan -ldl -lpthread -lX11 -lXxf86vm -lXrandr -lXi

1.1: main.cpp
	c++ $(CFLAGS) -o localvariables4 main.cpp $(LDFLAGS)

.PHONY: test clean

test: localvariables4
	./localvariables4

clean:
	rm -f localvariables4
