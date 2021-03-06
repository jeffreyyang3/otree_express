# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-05-06 23:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models
import otree_save_the_change.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emo_quest_panas_mauss_discrete2_group', to='otree.Session')),
            ],
            options={
                'db_table': 'emo_quest_panas_mauss_discrete2_group',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_gbat_arrived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('_gbat_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('time_EmoQuestPage1', otree.db.models.LongStringField(null=True)),
                ('time_EmoQuestPage2', otree.db.models.LongStringField(null=True)),
                ('panasmauss_Active', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Active')),
                ('panasmauss_Excited', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Excited')),
                ('panasmauss_Angry', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Angry')),
                ('panasmauss_Interested', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Interested')),
                ('panasmauss_Sad', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Sad')),
                ('panasmauss_Gratitude', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Gratitude')),
                ('panasmauss_Upset', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Upset')),
                ('panasmauss_Proud', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Proud')),
                ('panasmauss_Happy', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Happy')),
                ('panasmauss_Hostile', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Hostile')),
                ('panasmauss_Anxious', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Anxious')),
                ('panasmauss_Strong', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Strong')),
                ('panasmauss_Loving', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Loving')),
                ('panasmauss_Distressed', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Distressed')),
                ('panasmauss_Guilty', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Guilty')),
                ('panasmauss_Calm', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Calm')),
                ('panasmauss_Nervous', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Nervous')),
                ('panasmauss_Scared', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Scared')),
                ('panasmauss_Determined', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Determined')),
                ('panasmauss_Annoyed', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Annoyed')),
                ('panasmauss_Inspired', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Inspired')),
                ('panasmauss_Positive (feel good)', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Positive (feel good)')),
                ('panasmauss_Alert', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Alert')),
                ('panasmauss_Energetic', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Energetic')),
                ('panasmauss_Negative (feel bad)', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Negative (feel bad)')),
                ('panasmauss_Jittery', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Jittery')),
                ('panasmauss_Ashamed', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Ashamed')),
                ('panasmauss_Amused', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Amused')),
                ('panasmauss_Attentive', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Attentive')),
                ('panasmauss_Irritable', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Irritable')),
                ('panasmauss_Enthusiastic', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Enthusiastic')),
                ('panasmauss_Afraid', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='Afraid')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='emo_quest_panas_mauss_discrete2.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emo_quest_panas_mauss_discrete2_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emo_quest_panas_mauss_discrete2_player', to='otree.Session')),
            ],
            options={
                'db_table': 'emo_quest_panas_mauss_discrete2_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emo_quest_panas_mauss_discrete2_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'emo_quest_panas_mauss_discrete2_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emo_quest_panas_mauss_discrete2.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emo_quest_panas_mauss_discrete2.Subsession'),
        ),
    ]
