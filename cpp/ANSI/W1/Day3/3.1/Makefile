CFLAGS = -std=c++03 -O2
LDFLAGS = -lglfw -lvulkan -ldl -lpthread -lX11 -lXxf86vm -lXrandr -lXi

1.1: main.cpp
	c++ $(CFLAGS) -o sizeofvars main.cpp $(LDFLAGS)

.PHONY: test clean

test: sizeofvars
	./sizeofvars

clean:
	rm -f sizeofvars
