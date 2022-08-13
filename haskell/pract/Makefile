run: clean hello linregcpp 
	./hello
	./linregcpp.out
	python dot.py
	cargo run

   





rust: src/main.rs
	cargo build --release

hello: hello.hs
	ghc hello.hs
linregcpp: linreg.cpp
	g++ linreg.cpp -o linregcpp.out
	
clean:
	cargo clean
	rm -f  *.o
	rm -f *.out
