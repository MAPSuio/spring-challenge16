# Antar at ag er installert (ligger i /snacks/bin/ på ifi's login-servere)
time curl -s https://kernel.org/pub/linux/kernel/v4.x/linux-4.0.4.tar.xz | tar xJf - -O | ag -ci crap | paste -sd+ - | bc
