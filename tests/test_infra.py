import pytest

def test_elastichead_server_running_and_enabled(Command,Service):
  # Check that docker service is running and enabled
  docker_service = Service("docker")
  assert docker_service.is_running
  assert docker_service.is_enabled
  # Check that elastichead service is running and enabled
  elastichead_service = Service("elastichead")
  assert elastichead_service.is_running
  assert elastichead_service.is_enabled

  # Check that elastichead-cli ping
  elastichead_output = Command.check_output("docker exec elastichead elastichead-cli ping")
  assert elastichead_output == "PONG"

def test_elastichead_start_stop(Command,Service):
  Command.run_expect([0],"systemctl stop elastichead")
  elastichead_service = Service("elastichead")
  assert not elastichead_service.is_running
  Command.run_expect([0],"systemctl start elastichead")
  assert elastichead_service.is_running
  Command.run_expect([0],"systemctl restart elastichead")
  assert elastichead_service.is_running
  elastichead_output = Command.check_output("docker exec elastichead elastichead-cli ping")
  assert elastichead_output == "PONG"
