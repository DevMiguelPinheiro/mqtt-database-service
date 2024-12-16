from containers import Container


def main():
    container = Container()
    mqtt_service = container.mqtt_service()
    mqtt_service.start()


if __name__ == "__main__":
    main()
