{%- set source = salt['pillar.get']('dirs:source', '') %}
{%- set target = salt['pillar.get']('dirs:target', '') %}

bash-backup-tool:
  cron.present:
    - name: /etc/backup_tools/bash_backup
    - hour: 5
  file.managed:
    - user: root
    - name: /etc/backup_tools/bash_backup
    - source: salt://{{ tpldir }}/backup_tools/files/bash_backup
    - makedirs:
      - True

py-backup-tool:
  cron.present:
    - name: /usr/bin/python3 /etc/backup_tools/python_backup.py -s {{ source }} -t {{ target }}
    - hour: 5
  file.managed:
    - name: /etc/backup_tools/python_backup.py
    - source: salt://{{ tpldir }}/backup_tools/files/python_backup.py
    - makedirs:
      - True

