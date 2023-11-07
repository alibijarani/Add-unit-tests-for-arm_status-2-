import rclpy
import pytest
from spot_arm_status.spot_arm_status_pub import JointStateSubscriber


@pytest.fixture(scope="module")
def ros_init():
    rclpy.init()


    def test_arm_stowed_evaluation_when_arm_is_stowed_should_return_true(self):
        # given
        arm_stowed_values = [
            -0.0001456737518310547,
            -3.115017890930176,
            0.0,
            3.132694959640503,
            1.570010781288147,
            0.0025632381439208984,
            -1.56974196434021,
        ]
        node = JointStateSubscriber()
        # expected
        assert node.checking_if_the_position_of_arm_is_stowed_or_not(arm_stowed_values) is True

    def test_arm_stowed_evaluation_when_arm_is_not_stowed_should_return_false(self):
        
        

        # given
        arm_values = [0, 1, 2, 3, 4, 5, 6]
        node = JointStateSubscriber()
        # expected
        assert node.checking_if_the_position_of_arm_is_stowed_or_not(arm_values) is False


    def test_gripper_evaluation_when_gripper_is_close_to_closed_position_should_return_true(self):
        
        # given
        gripper_position = -0.02
        node = JointStateSubscriber()
        # expected
        assert node.checking_if_the_gripper_is_open_or_closed_position(gripper_position) is True

    def test_gripper_evaluation_when_gripper_is_close_to_open_position_should_return_false():
    #given
        gripper_position = 0.02
        node = JointStateSubscriber()
        # expected
        assert node.checking_if_the_gripper_is_open_or_closed_position(gripper_position) is False

