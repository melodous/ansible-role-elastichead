def test_socket(Socket):
    # Check elastichead port is up and running
    assert Socket("tcp://0.0.0.0:9100").is_listening


def test_elastichead_server_running_and_enabled(Command, Service):
    # Check that docker service is running and enabled
    docker_service = Service("docker")
    assert docker_service.is_running
    assert docker_service.is_enabled
    # Check that elastichead service is running and enabled
    elastichead_service = Service("elastichead")
    assert elastichead_service.is_running
    assert elastichead_service.is_enabled


def test_elastichead_start_stop(Command, Service):
    Command.run_expect([0], "systemctl stop elastichead")
    elastichead_service = Service("elastichead")
    assert not elastichead_service.is_running
    Command.run_expect([0], "systemctl start elastichead")
    assert elastichead_service.is_running
    Command.run_expect([0], "systemctl restart elastichead")
    assert elastichead_service.is_running
