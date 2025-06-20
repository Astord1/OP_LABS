from generator_lib.reactive import EventEmitter

def listener_one(data):
    print(f"[Listener 1] Received: {data}")

def listener_two(data):
    print(f"[Listener 2] Got it: {data}")

def main():
    bus = EventEmitter()

    unsub_one = bus.subscribe("ping", listener_one)
    unsub_two = bus.subscribe("ping", listener_two)

    bus.emit("ping", "Hello listeners!")

    unsub_one()

    bus.emit("ping", "Only Listener 2 should see this.")

if __name__ == "__main__":
    main()
