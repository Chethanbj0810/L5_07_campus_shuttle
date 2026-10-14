"""Campus shuttle timetable and fleet tracking system."""

import json
import secrets
from datetime import datetime
from pathlib import Path

MIN_CAPACITY = 10

routes = {
    "R1": {"name": "Main Gate - Library", "trips": []},
    "R2": {"name": "Hostel - Sports Complex", "trips": []},
    "R3": {"name": "Admin Block - Metro", "trips": []},
}


def add_trip_log(route_id, passenger_count, logs=None):
    """Record a valid passenger count for a shuttle trip."""
    if route_id not in routes:
        raise ValueError(f"Unknown route: {route_id}")

    if (
        not isinstance(passenger_count, int)
        or isinstance(passenger_count, bool)
        or passenger_count < 0
    ):
        raise ValueError("Passenger count must be a non-negative integer.")

    if logs is None:
        logs = []

    routes[route_id]["trips"].append(passenger_count)
    logs.append(f"{datetime.now()}: {route_id} carried {passenger_count}")
    return logs


def remove_route(route_id):
    """Remove a route if it exists."""
    if route_id not in routes:
        raise ValueError(f"Unknown route: {route_id}")
    del routes[route_id]


def average_load(route_id):
    """Calculate the average passenger count for a route."""
    if route_id not in routes:
        raise ValueError(f"Unknown route: {route_id}")

    trips = routes[route_id]["trips"]
    if not trips:
        return 0.0

    return sum(trips) / len(trips)


def underused_routes():
    """Return routes whose average load is below minimum capacity."""
    return [
        route_id
        for route_id in routes
        if average_load(route_id) < MIN_CAPACITY
    ]


def assign_driver(route_id):
    """Assign a driver to a valid shuttle route."""
    if route_id not in routes:
        raise ValueError(f"Unknown route: {route_id}")

    drivers = ["Prakash", "Leela", "Imran", "Tom"]
    return secrets.choice(drivers)


def sync_fleet_data(file="fleet.json"):
    """Save routes to JSON and return the saved fleet data."""
    file_path = Path(file)

    with file_path.open("w", encoding="utf-8") as fleet_file:
        json.dump(routes, fleet_file, indent=4)

    with file_path.open("r", encoding="utf-8") as fleet_file:
        return json.load(fleet_file)


def main():
    """Run a demonstration of the campus shuttle tracker."""
    add_trip_log("R1", 32)
    add_trip_log("R1", 28)
    add_trip_log("R2", 4)
    add_trip_log("R2", 6)
    add_trip_log("R3", 15)

    print("Driver for R1:", assign_driver("R1"))
    print("Underused:", underused_routes())
    print("R1 average:", average_load("R1"))

    sync_fleet_data()

    choice = input("Route to look up (Enter for R2): ").strip() or "R2"

    if choice not in routes:
        print(f"Unknown route: {choice}")
        return

    print("Trips on", choice, ":", routes[choice]["trips"])
    print("R3 average:", average_load("R3"))


if __name__ == "__main__":
    main()
