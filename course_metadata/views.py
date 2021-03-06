from course_metadata.models import CourseSetting
from course_metadata.serializers import CourseSettingSerializer
from edx_solutions_api_integration.permissions import SecureRetrieveUpdateAPIView
from opaque_keys.edx.keys import CourseKey


class CourseSettingView(SecureRetrieveUpdateAPIView):
    """
    **Use Case**

        Create course settings

    **Example Requests**

        POST /api/server/courses_metadata/{course_id}/settings

    **Request Params**

        **POST**

        -id: course id

    **Response Values**

        **POST**

        If the request is successful, the request returns an HTTP 200 "OK" response.
    """
    serializer_class = CourseSettingSerializer
    queryset = CourseSetting.objects.all()

    def get_object(self):
        course_id = CourseKey.from_string(self.kwargs['course_id'])
        setting, __ = CourseSetting.objects.get_or_create(id=course_id)
        return setting
