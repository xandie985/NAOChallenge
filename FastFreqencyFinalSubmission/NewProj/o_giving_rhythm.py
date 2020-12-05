from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.166667, 0.433333, 0.7, 0.966667, 1.23333, 1.5, 1.76667, 2.03333, 2.3])
keys.append([-0.356047, 0.270526, -0.356047, 0.270526, -0.356047, 0.270526, -0.356047, 0.270526, 0])

names.append("HeadYaw")
times.append([0.166667, 0.433333, 0.7, 0.966667, 1.23333, 1.5, 1.76667, 2.03333, 2.3])
keys.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

names.append("LAnklePitch")
times.append([0.166667, 0.433333, 0.7, 0.966667, 1.23333, 1.5, 1.76667, 2.03333, 2.3])
keys.append([-0.348738, -0.348738, -0.348738, -0.348738, -0.348738, -0.348738, -0.348738, -0.348738, -0.348738])

names.append("LAnkleRoll")
times.append([0.166667, 0.433333, 0.7, 0.966667, 1.23333, 1.5, 1.76667, 2.03333, 2.3])
keys.append([-0.00852969, -0.00852969, -0.00852969, -0.00852969, -0.00852969, -0.00852969, -0.00852969, -0.00852969, -0.00852969])

names.append("LElbowRoll")
times.append([0.166667, 0.433333, 0.7, 0.966667, 1.23333, 1.5, 1.76667, 2.03333, 2.3])
keys.append([-1.00126, -1.00126, -1.00126, -1.00126, -1.00126, -1.00126, -1.00126, -1.00126, -1.00126])

names.append("LElbowYaw")
times.append([0.166667, 0.433333, 0.7, 0.966667, 1.23333, 1.5, 1.76667, 2.03333, 2.3])
keys.append([-1.39872, -1.39872, -1.39872, -1.39872, -1.39872, -1.39872, -1.39872, -1.39872, -1.39872])

names.append("LHand")
times.append([0.166667, 0.433333, 0.7, 0.966667, 1.23333, 1.5, 1.76667, 2.03333, 2.3])
keys.append([0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25])

names.append("LHipPitch")
times.append([0.166667, 0.433333, 0.7, 0.966667, 1.23333, 1.5, 1.76667, 2.03333, 2.3])
keys.append([-0.448337, -0.448337, -0.448337, -0.448337, -0.448337, -0.448337, -0.448337, -0.448337, -0.448337])

names.append("LHipRoll")
times.append([0.166667, 0.433333, 0.7, 0.966667, 1.23333, 1.5, 1.76667, 2.03333, 2.3])
keys.append([0.000286866, 0.000286866, 0.000286866, 0.000286866, 0.000286866, 0.000286866, 0.000286866, 0.000286866, 0.000286866])

names.append("LHipYawPitch")
times.append([0.166667, 0.433333, 0.7, 0.966667, 1.23333, 1.5, 1.76667, 2.03333, 2.3])
keys.append([-0.000487671, -0.000487671, -0.000487671, -0.000487671, -0.000487671, -0.000487671, -0.000487671, -0.000487671, -0.000487671])

names.append("LKneePitch")
times.append([0.166667, 0.433333, 0.7, 0.966667, 1.23333, 1.5, 1.76667, 2.03333, 2.3])
keys.append([0.697734, 0.697734, 0.697734, 0.697734, 0.697734, 0.697734, 0.697734, 0.697734, 0.697734])

names.append("LShoulderPitch")
times.append([0.166667, 0.433333, 0.7, 0.966667, 1.23333, 1.5, 1.76667, 2.03333, 2.3])
keys.append([1.39727, 1.39727, 1.39727, 1.39727, 1.39727, 1.39727, 1.39727, 1.39727, 1.39727])

names.append("LShoulderRoll")
times.append([0.166667, 0.433333, 0.7, 0.966667, 1.23333, 1.5, 1.76667, 2.03333, 2.3])
keys.append([0.301284, 0.301284, 0.301284, 0.301284, 0.301284, 0.301284, 0.301284, 0.301284, 0.301284])

names.append("LWristYaw")
times.append([0.166667, 0.433333, 0.7, 0.966667, 1.23333, 1.5, 1.76667, 2.03333, 2.3])
keys.append([-0.00728834, -0.00728834, -0.00728834, -0.00728834, -0.00728834, -0.00728834, -0.00728834, -0.00728834, -0.00728834])

names.append("RAnklePitch")
times.append([0.166667, 0.433333, 0.7, 0.966667, 1.23333, 1.5, 1.76667, 2.03333, 2.3])
keys.append([-0.5044, -0.354476, -0.5044, -0.354476, -0.5044, -0.354476, -0.5044, -0.354476, -0.355665])

names.append("RAnkleRoll")
times.append([0.166667, 0.433333, 0.7, 0.966667, 1.23333, 1.5, 1.76667, 2.03333, 2.3])
keys.append([0.00589853, 0.00589853, 0.00589853, 0.00589853, 0.00589853, 0.00589853, 0.00589853, 0.00589853, 0.00589853])

names.append("RElbowRoll")
times.append([0.166667, 0.433333, 0.7, 0.966667, 1.23333, 1.5, 1.76667, 2.03333, 2.3])
keys.append([1.00126, 1.00126, 1.00126, 1.00126, 1.00126, 1.00126, 1.00126, 1.00126, 1.00126])

names.append("RElbowYaw")
times.append([0.166667, 0.433333, 0.7, 0.966667, 1.23333, 1.5, 1.76667, 2.03333, 2.3])
keys.append([1.39872, 1.39872, 1.39872, 1.39872, 1.39872, 1.39872, 1.39872, 1.39872, 1.39872])

names.append("RHand")
times.append([0.166667, 0.433333, 0.7, 0.966667, 1.23333, 1.5, 1.76667, 2.03333, 2.3])
keys.append([0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25])

names.append("RHipPitch")
times.append([0.166667, 0.433333, 0.7, 0.966667, 1.23333, 1.5, 1.76667, 2.03333, 2.3])
keys.append([-0.448337, -0.448337, -0.448337, -0.448337, -0.448337, -0.448337, -0.448337, -0.448337, -0.448337])

names.append("RHipRoll")
times.append([0.166667, 0.433333, 0.7, 0.966667, 1.23333, 1.5, 1.76667, 2.03333, 2.3])
keys.append([-0.0715585, -0.0628318, -0.0715585, -0.0628318, -0.0715585, -0.0628318, -0.0715585, -0.0628318, 0])

names.append("RHipYawPitch")
times.append([0.166667, 0.433333, 0.7, 0.966667, 1.23333, 1.5, 1.76667, 2.03333, 2.3])
keys.append([-0.000487671, -0.000487671, -0.000487671, -0.000487671, -0.000487671, -0.000487671, -0.000487671, -0.000487671, -0.000487671])

names.append("RKneePitch")
times.append([0.166667, 0.433333, 0.7, 0.966667, 1.23333, 1.5, 1.76667, 2.03333, 2.3])
keys.append([0.699999, 0.699999, 0.699999, 0.699999, 0.699999, 0.699999, 0.699999, 0.699999, 0.699999])

names.append("RShoulderPitch")
times.append([0.166667, 0.433333, 0.7, 0.966667, 1.23333, 1.5, 1.76667, 2.03333, 2.3])
keys.append([1.39727, 1.39727, 1.39727, 1.39727, 1.39727, 1.39727, 1.39727, 1.39727, 1.39727])

names.append("RShoulderRoll")
times.append([0.166667, 0.433333, 0.7, 0.966667, 1.23333, 1.5, 1.76667, 2.03333, 2.3])
keys.append([-0.301284, -0.301284, -0.301284, -0.301284, -0.301284, -0.301284, -0.301284, -0.301284, -0.301284])

names.append("RWristYaw")
times.append([0.166667, 0.433333, 0.7, 0.966667, 1.23333, 1.5, 1.76667, 2.03333, 2.3])
keys.append([0.00728834, 0.00728834, 0.00728834, 0.00728834, 0.00728834, 0.00728834, 0.00728834, 0.00728834, 0.00728834])


# copy paste the printed value and uncomment
keysValue = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
finalPositionValue = [-1.39872, 0.25, 0.000286866, 0.697734, 1.39727, 0.301284, -0.00728834]