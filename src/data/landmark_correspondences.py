import numpy as np
landmark_points_68 = np.array([162,234,93,58,172,136,149,148,152,377,378,365,397,288,323,454,389,71,63,105,66,107,336,
                  296,334,293,301,168,197,5,4,75,97,2,326,305,33,160,158,133,153,144,362,385,387,263,373,
                  380,61,39,37,0,267,269,291,405,314,17,84,181,78,82,13,312,308,317,14,87])

# landmark_points_68_new=landmark_points_68[:48]
# landmark_points_68_new=np.append(landmark_points_68_new,landmark_points_68[51])
# landmark_points_68_new=np.append(landmark_points_68_new,landmark_points_68[54])
# landmark_points_68_new=np.append(landmark_points_68_new,landmark_points_68[57])
# landmark_points_68_new=np.append(landmark_points_68_new,landmark_points_68[60])
# landmark_points_68_new=np.append(landmark_points_68_new,landmark_points_68[62])
# landmark_points_68_new=np.append(landmark_points_68_new,landmark_points_68[64])
# landmark_points_68_new=np.append(landmark_points_68_new,landmark_points_68[66])
# landmark_points_68=landmark_points_68_new

landmark_points_68_reduced = landmark_points_68[27:]