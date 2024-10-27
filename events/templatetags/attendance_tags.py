from django import template

register = template.Library()

@register.filter
def get_attendance_status(attendance_dict, event_id):
    # event_idに対応する出席状況を取得
    return attendance_dict.get(event_id, "未回答")